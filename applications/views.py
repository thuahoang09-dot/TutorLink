from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application
from class_requests.models import ClassRequest
from matched_classes.models import MatchedClass

@login_required
def apply_class(request, class_id):
    if not request.user.profile.is_tutor:
        messages.error(request, 'Chỉ có tài khoản Gia sư mới có thể ứng tuyển nhận lớp.')
        return redirect('class_requests:class_detail', pk=class_id)

    tutor_profile = getattr(request.user, 'tutor_profile', None)
    if not tutor_profile or not tutor_profile.is_profile_completed:
        messages.warning(request, 'Bạn cần cập nhật đầy đủ hồ sơ gia sư trước khi ứng tuyển nhận lớp.')
        return redirect('tutors:edit_tutor_profile')

    if tutor_profile.approval_status != 'approved':
        if tutor_profile.approval_status == 'pending':
            messages.info(request, 'Hồ sơ gia sư của bạn đang chờ Ban Quản Trị (Admin) phê duyệt. Bạn sẽ có thể nhận lớp ngay sau khi được duyệt thành công.')
        else:
            messages.error(request, 'Hồ sơ gia sư của bạn chưa được phê duyệt. Vui lòng cập nhật lại thông tin hồ sơ.')
        return redirect('class_requests:class_detail', pk=class_id)

    class_request = get_object_or_404(ClassRequest, pk=class_id)

    if class_request.status != 'pending':
        messages.warning(request, 'Lớp học này đã đóng hoặc đã được ghép gia sư.')
        return redirect('class_requests:class_detail', pk=class_id)

    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        proposed_price = request.POST.get('proposed_price', '').strip()

        if not message:
            messages.error(request, 'Vui lòng nhập lời nhắn giới thiệu bản thân.')
            return redirect('class_requests:class_detail', pk=class_id)

        price = None
        if proposed_price:
            try:
                price = int(proposed_price)
            except ValueError:
                price = class_request.budget

        app, created = Application.objects.get_or_create(
            class_request=class_request,
            tutor=request.user,
            defaults={
                'message': message,
                'proposed_price': price,
                'status': 'pending'
            }
        )

        if not created:
            app.message = message
            if price:
                app.proposed_price = price
            app.status = 'pending'
            app.save()
            messages.info(request, 'Bạn đã cập nhật lại yêu cầu nhận lớp thành công! Yêu cầu đã được chuyển thẳng tới học sinh.')
        else:
            messages.success(request, 'Gửi yêu cầu nhận lớp thành công! Quyền duyệt đã được gửi thẳng tới học sinh để duyệt ghép lớp.')

        # Gửi thông báo chuẩn Facebook tới Học sinh (Gửi thẳng quyền duyệt cho học sinh, không cần admin)
        try:
            from accounts.models import create_notification
            subject_name = class_request.subject.name if class_request.subject else 'của bạn'
            tutor_name = request.user.profile.full_name or request.user.username
            create_notification(
                recipient=class_request.student,
                sender=request.user,
                notification_type='apply_class',
                title='Có gia sư muốn nhận lớp - Chờ bạn duyệt',
                message=f"Gia sư {tutor_name} đã gửi yêu cầu nhận lớp môn {subject_name} ('{class_request.title}'). Bạn hãy vào duyệt và ghép lớp ngay nhé!",
                link=f"/classes/{class_request.id}/#applications-section"
            )
        except Exception:
            pass

    return redirect('class_requests:class_detail', pk=class_id)

@login_required
def accept_application(request, application_id):
    application = get_object_or_404(
        Application.objects.select_related('class_request', 'tutor', 'class_request__student'),
        pk=application_id
    )
    class_request = application.class_request

    # Check permission
    if class_request.student != request.user and not request.user.profile.is_admin_user:
        messages.error(request, 'Bạn không có quyền duyệt đơn ứng tuyển này.')
        return redirect('class_requests:class_detail', pk=class_request.id)

    if request.method == 'POST':
        # Accept this application
        application.status = 'accepted'
        application.save()

        # Get list of other pending applicants to notify rejection
        other_applicants = list(
            class_request.applications.filter(status='pending')
            .exclude(pk=application.pk)
            .select_related('tutor')
        )

        # Reject remaining pending applications for this class
        class_request.applications.filter(status='pending').exclude(pk=application.pk).update(status='rejected')

        # Update class request status
        class_request.status = 'accepted'
        class_request.save()

        # Create MatchedClass automatically
        hourly_rate = application.proposed_price if application.proposed_price else class_request.budget
        matched_class, _ = MatchedClass.objects.get_or_create(
            class_request=class_request,
            defaults={
                'student': class_request.student,
                'tutor': application.tutor,
                'subject': class_request.subject,
                'schedule': class_request.schedule,
                'hourly_rate': hourly_rate,
                'teaching_method': class_request.teaching_method,
                'status': 'in_progress',
            }
        )

        # Gửi thông báo chuẩn Facebook tới Gia sư được nhận lớp
        try:
            from accounts.models import create_notification
            student_name = request.user.profile.full_name or request.user.username
            subject_name = class_request.subject.name if class_request.subject else ''
            create_notification(
                recipient=application.tutor,
                sender=request.user,
                notification_type='accept_application',
                title='Chúc mừng! Học sinh đã nhận bạn làm gia sư',
                message=f"Học sinh {student_name} đã đồng ý nhận bạn dạy lớp môn {subject_name}! Lớp học đã được kết nối.",
                link=f"/matched-classes/{matched_class.id}/"
            )

            # Thông báo tới các gia sư khác chưa được chọn
            for other_app in other_applicants:
                if other_app.tutor != application.tutor:
                    create_notification(
                        recipient=other_app.tutor,
                        sender=request.user,
                        notification_type='reject_application',
                        title='Thông báo kết quả ứng tuyển lớp học',
                        message=f"Lớp môn {subject_name} bạn ứng tuyển đã tìm được gia sư phù hợp.",
                        link=f"/classes/{class_request.id}/"
                    )
        except Exception:
            pass

        messages.success(request, f'Đã chọn gia sư {application.tutor.profile.full_name or application.tutor.username} và ghép lớp thành công!')
        return redirect('matched_classes:class_detail', pk=matched_class.pk)

    return redirect('class_requests:class_detail', pk=class_request.id)

@login_required
def reject_application(request, application_id):
    application = get_object_or_404(Application.objects.select_related('class_request'), pk=application_id)
    class_request = application.class_request

    if class_request.student != request.user and not request.user.profile.is_admin_user:
        messages.error(request, 'Bạn không có quyền thực hiện thao tác này.')
        return redirect('class_requests:class_detail', pk=class_request.id)

    if request.method == 'POST':
        application.status = 'rejected'
        application.save()
        messages.info(request, 'Đã từ chối yêu cầu nhận lớp của gia sư.')
        if request.POST.get('next') == 'dashboard':
            return redirect('dashboard:student_dashboard')

    return redirect('class_requests:class_detail', pk=class_request.id)

@login_required
def my_applications(request):
    if not request.user.profile.is_tutor:
        messages.error(request, 'Chức năng này chỉ dành cho tài khoản gia sư.')
        return redirect('home')

    apps = Application.objects.filter(tutor=request.user).select_related(
        'class_request', 'class_request__student', 'class_request__student__profile', 'class_request__subject'
    ).order_by('-created_at')

    return render(request, 'applications/my_applications.html', {'applications': apps})
