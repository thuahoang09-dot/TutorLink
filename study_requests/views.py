from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StudyRequest
from .forms import StudyRequestForm
from tutors.models import TutorProfile
from matched_classes.models import MatchedClass

from class_requests.views import get_default_timetable

@login_required
def create_request(request, tutor_id):
    tutor_profile = get_object_or_404(TutorProfile.objects.select_related('user', 'user__profile'), pk=tutor_id)
    tutor_user = tutor_profile.user

    if request.user == tutor_user:
        messages.warning(request, 'Bạn không thể tự gửi yêu cầu học cho chính mình!')
        return redirect('tutors:tutor_detail', pk=tutor_id)

    if not (request.user.profile.is_student or request.user.profile.is_admin_user):
        messages.warning(request, 'Chức năng gửi yêu cầu học dành cho tài khoản Học sinh.')
        return redirect('tutors:tutor_detail', pk=tutor_id)

    if request.method == 'POST':
        form = StudyRequestForm(request.POST, tutor=tutor_user)
        if form.is_valid():
            study_req = form.save(commit=False)
            study_req.student = request.user
            study_req.tutor = tutor_user
            study_req.status = 'pending'
            study_req.save()

            # Gửi thông báo chuẩn Facebook tới Gia sư
            try:
                from accounts.models import create_notification
                student_name = request.user.profile.full_name or request.user.username
                sub_name = study_req.subject.name if study_req.subject else ''
                create_notification(
                    recipient=tutor_user,
                    sender=request.user,
                    notification_type='study_request',
                    title='Yêu cầu học mới từ học sinh',
                    message=f"Học sinh {student_name} vừa gửi yêu cầu học kèm môn {sub_name} cho bạn.",
                    link="/tutor/requests/"
                )
            except Exception:
                pass

            messages.success(request, f'Đã gửi yêu cầu học trực tiếp tới gia sư {tutor_profile.full_name}! Vui lòng chờ phản hồi.')
            return redirect('study_requests:student_requests')
    else:
        form = StudyRequestForm(tutor=tutor_user)

    timetable = get_default_timetable(request.POST.get('schedule', '') if request.method == 'POST' else '')

    return render(request, 'study_requests/create_request.html', {
        'form': form,
        'tutor_profile': tutor_profile,
        'timetable': timetable,
    })

@login_required
def tutor_requests(request):
    if not request.user.profile.is_tutor:
        messages.error(request, 'Chức năng này chỉ dành cho tài khoản gia sư.')
        return redirect('home')

    requests_list = StudyRequest.objects.filter(tutor=request.user).select_related(
        'student', 'student__profile', 'subject'
    ).order_by('-created_at')

    return render(request, 'study_requests/tutor_requests.html', {'requests_list': requests_list})

@login_required
def student_requests(request):
    requests_list = StudyRequest.objects.filter(student=request.user).select_related(
        'tutor', 'tutor__profile', 'tutor__tutor_profile', 'subject'
    ).order_by('-created_at')

    return render(request, 'study_requests/student_requests.html', {'requests_list': requests_list})

@login_required
def accept_request(request, request_id):
    study_req = get_object_or_404(StudyRequest, pk=request_id, tutor=request.user)

    if request.method == 'POST':
        study_req.status = 'accepted'
        study_req.save()

        # Create MatchedClass
        hourly_rate = study_req.tutor.tutor_profile.price_per_hour if hasattr(study_req.tutor, 'tutor_profile') else 150000
        matched_class, _ = MatchedClass.objects.get_or_create(
            study_request=study_req,
            defaults={
                'student': study_req.student,
                'tutor': study_req.tutor,
                'subject': study_req.subject,
                'schedule': study_req.schedule,
                'hourly_rate': hourly_rate,
                'teaching_method': study_req.teaching_method,
                'status': 'in_progress',
            }
        )

        # Gửi thông báo chuẩn Facebook tới Học sinh
        try:
            from accounts.models import create_notification
            tutor_name = request.user.profile.full_name or request.user.username
            sub_name = study_req.subject.name if study_req.subject else ''
            create_notification(
                recipient=study_req.student,
                sender=request.user,
                notification_type='accept_request',
                title='Gia sư đã nhận yêu cầu dạy học!',
                message=f"Gia sư {tutor_name} đã đồng ý nhận yêu cầu học môn {sub_name} của bạn! Lớp học đã được kết nối.",
                link=f"/matched-classes/{matched_class.id}/"
            )
        except Exception:
            pass

        messages.success(request, f'Đã đồng ý yêu cầu từ học sinh {study_req.student.profile.full_name or study_req.student.username}. Lớp học mới đã được tạo!')
        return redirect('matched_classes:class_detail', pk=matched_class.pk)

    return redirect('study_requests:tutor_requests')

@login_required
def reject_request(request, request_id):
    study_req = get_object_or_404(StudyRequest, pk=request_id, tutor=request.user)

    if request.method == 'POST':
        study_req.status = 'rejected'
        study_req.save()

        # Gửi thông báo tới Học sinh
        try:
            from accounts.models import create_notification
            tutor_name = request.user.profile.full_name or request.user.username
            sub_name = study_req.subject.name if study_req.subject else ''
            create_notification(
                recipient=study_req.student,
                sender=request.user,
                notification_type='reject_request',
                title='Cập nhật về yêu cầu học kèm',
                message=f"Gia sư {tutor_name} không thể nhận yêu cầu học môn {sub_name} vào thời điểm này.",
                link="/student/requests/"
            )
        except Exception:
            pass

        messages.info(request, 'Đã từ chối yêu cầu học.')

    return redirect('study_requests:tutor_requests')
