from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import UserProfile
from tutors.models import TutorProfile, Subject
from class_requests.models import ClassRequest
from applications.models import Application
from study_requests.models import StudyRequest
from matched_classes.models import MatchedClass
from reviews.models import Review

# --- Student Dashboard ---
@login_required
def student_dashboard(request):
    if not (request.user.profile.is_student or request.user.profile.is_admin_user):
        messages.warning(request, 'Trang này dành cho học sinh.')
        return redirect('home')

    my_posts = ClassRequest.objects.filter(student=request.user).select_related('subject').order_by('-created_at')
    active_classes = MatchedClass.objects.filter(student=request.user, status='in_progress').select_related('tutor', 'subject')
    completed_classes = MatchedClass.objects.filter(student=request.user, status='completed')
    sent_requests = StudyRequest.objects.filter(student=request.user)

    # Pending applications from tutors for this student's posts
    pending_apps = Application.objects.filter(class_request__student=request.user, status='pending').select_related('class_request', 'tutor')

    return render(request, 'dashboard/student_dashboard.html', {
        'total_posts': my_posts.count(),
        'total_active_classes': active_classes.count(),
        'total_completed_classes': completed_classes.count(),
        'total_sent_requests': sent_requests.count(),
        'my_posts': my_posts[:5],
        'active_classes': active_classes[:5],
        'pending_apps': pending_apps[:5],
    })

# --- Tutor Dashboard ---
@login_required
def tutor_dashboard(request):
    if not (request.user.profile.is_tutor or request.user.profile.is_admin_user):
        messages.warning(request, 'Trang này dành cho gia sư.')
        return redirect('home')

    tutor_profile, _ = TutorProfile.objects.get_or_create(user=request.user)

    incoming_requests = StudyRequest.objects.filter(tutor=request.user, status='pending').select_related('student', 'subject')
    applied_classes = Application.objects.filter(tutor=request.user)
    active_classes = MatchedClass.objects.filter(tutor=request.user, status='in_progress').select_related('student', 'subject')
    completed_classes = MatchedClass.objects.filter(tutor=request.user, status='completed')
    reviews = Review.objects.filter(tutor=request.user).select_related('student')

    return render(request, 'dashboard/tutor_dashboard.html', {
        'tutor_profile': tutor_profile,
        'pending_requests_count': incoming_requests.count(),
        'applied_count': applied_classes.count(),
        'active_classes_count': active_classes.count(),
        'completed_classes_count': completed_classes.count(),
        'avg_rating': tutor_profile.get_average_rating(),
        'review_count': tutor_profile.get_review_count(),
        'incoming_requests': incoming_requests[:5],
        'active_classes': active_classes[:5],
        'recent_reviews': reviews[:5],
    })

# --- Admin Dashboard ---
@login_required
def admin_dashboard(request):
    if not request.user.profile.is_admin_user:
        messages.error(request, 'Bạn không có quyền truy cập trang quản trị.')
        return redirect('home')

    total_users = User.objects.count()
    total_students = UserProfile.objects.filter(role='student').count()
    total_tutors = UserProfile.objects.filter(role='tutor').count()
    pending_tutors = TutorProfile.objects.filter(approval_status='pending').count()
    total_posts = ClassRequest.objects.count()
    total_classes = MatchedClass.objects.count()
    total_reviews = Review.objects.count()

    recent_tutors = TutorProfile.objects.filter(approval_status='pending').select_related('user', 'user__profile')[:5]
    recent_posts = ClassRequest.objects.select_related('student', 'subject').order_by('-created_at')[:5]
    recent_classes = MatchedClass.objects.select_related('student', 'tutor', 'subject').order_by('-created_at')[:5]

    return render(request, 'dashboard/admin_dashboard.html', {
        'total_users': total_users,
        'total_students': total_students,
        'total_tutors': total_tutors,
        'pending_tutors': pending_tutors,
        'total_posts': total_posts,
        'total_classes': total_classes,
        'total_reviews': total_reviews,
        'recent_tutors': recent_tutors,
        'recent_posts': recent_posts,
        'recent_classes': recent_classes,
    })

@login_required
def admin_users(request):
    if not request.user.profile.is_admin_user:
        messages.error(request, 'Từ chối truy cập.')
        return redirect('home')

    users = User.objects.select_related('profile').order_by('-date_joined')
    role_filter = request.GET.get('role')
    if role_filter in ['student', 'tutor', 'admin']:
        users = users.filter(profile__role=role_filter)

    return render(request, 'dashboard/admin_users.html', {'users': users, 'role_filter': role_filter})

@login_required
def admin_toggle_lock(request, user_id):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    target_user = get_object_or_404(User, pk=user_id)
    if target_user.is_superuser:
        messages.error(request, 'Không thể khóa tài khoản Superuser.')
        return redirect('dashboard:admin_users')

    profile = target_user.profile
    profile.is_locked = not profile.is_locked
    profile.save()

    status_str = "khóa" if profile.is_locked else "mở khóa"
    messages.success(request, f'Đã {status_str} tài khoản {target_user.username} thành công.')
    return redirect('dashboard:admin_users')

@login_required
def admin_tutors(request):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    status_filter = request.GET.get('status', 'pending')
    tutors = TutorProfile.objects.select_related('user', 'user__profile').prefetch_related('subjects').order_by('-created_at')

    if status_filter in ['pending', 'approved', 'rejected']:
        tutors = tutors.filter(approval_status=status_filter)

    return render(request, 'dashboard/admin_tutors.html', {
        'tutors': tutors,
        'status_filter': status_filter
    })

@login_required
def admin_approve_tutor(request, tutor_id):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    tutor = get_object_or_404(TutorProfile, pk=tutor_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        feedback = request.POST.get('feedback', '').strip()

        if action == 'approve':
            tutor.approval_status = 'approved'
            messages.success(request, f'Đã phê duyệt hồ sơ gia sư {tutor.full_name}!')
            try:
                from accounts.models import create_notification
                create_notification(
                    recipient=tutor.user,
                    sender=request.user,
                    notification_type='system',
                    title='Hồ sơ gia sư đã được phê duyệt',
                    message='Chúc mừng! Hồ sơ gia sư của bạn đã được Ban Quản Trị phê duyệt thành công. Bạn đã có thể ứng tuyển nhận lớp ngay bây giờ.',
                    link='/classes/'
                )
            except Exception:
                pass
        elif action == 'reject':
            tutor.approval_status = 'rejected'
            messages.info(request, f'Đã từ chối hồ sơ gia sư {tutor.full_name}.')
            try:
                from accounts.models import create_notification
                msg_reason = f" Lý do: {feedback}" if feedback else " Vui lòng cập nhật lại thông tin hồ sơ theo yêu cầu."
                create_notification(
                    recipient=tutor.user,
                    sender=request.user,
                    notification_type='system',
                    title='Hồ sơ gia sư chưa được phê duyệt',
                    message=f"Hồ sơ gia sư của bạn chưa được phê duyệt.{msg_reason}",
                    link='/tutors/edit-profile/'
                )
            except Exception:
                pass

        tutor.admin_feedback = feedback
        tutor.save()

    return redirect('dashboard:admin_tutors')

@login_required
def admin_posts(request):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    posts = ClassRequest.objects.select_related('student', 'subject').order_by('-created_at')
    return render(request, 'dashboard/admin_posts.html', {'posts': posts})

@login_required
def admin_classes(request):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    classes = MatchedClass.objects.select_related('student', 'tutor', 'subject').order_by('-created_at')
    return render(request, 'dashboard/admin_classes.html', {'classes': classes})

@login_required
def admin_reviews(request):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    reviews = Review.objects.select_related('student', 'tutor', 'matched_class').order_by('-created_at')
    return render(request, 'dashboard/admin_reviews.html', {'reviews': reviews})

@login_required
def admin_delete_review(request, review_id):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Đã xóa đánh giá vi phạm thành công.')

    return redirect('dashboard:admin_reviews')

@login_required
def admin_statistics(request):
    if not request.user.profile.is_admin_user:
        return redirect('home')

    subjects_stats = Subject.objects.all()
    # List statistics
    context = {
        'total_users': User.objects.count(),
        'total_students': UserProfile.objects.filter(role='student').count(),
        'total_tutors': UserProfile.objects.filter(role='tutor').count(),
        'approved_tutors': TutorProfile.objects.filter(approval_status='approved').count(),
        'pending_tutors': TutorProfile.objects.filter(approval_status='pending').count(),
        'total_posts': ClassRequest.objects.count(),
        'total_applications': Application.objects.count(),
        'total_study_requests': StudyRequest.objects.count(),
        'total_matched_classes': MatchedClass.objects.count(),
        'in_progress_classes': MatchedClass.objects.filter(status='in_progress').count(),
        'completed_classes': MatchedClass.objects.filter(status='completed').count(),
        'total_reviews': Review.objects.count(),
        'subjects': subjects_stats,
    }
    return render(request, 'dashboard/admin_statistics.html', context)
