from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MatchedClass

@login_required
def student_classes(request):
    if not (request.user.profile.is_student or request.user.profile.is_admin_user):
        messages.error(request, 'Trang này dành cho tài khoản học sinh.')
        return redirect('home')

    classes = MatchedClass.objects.filter(student=request.user).select_related(
        'tutor', 'tutor__profile', 'tutor__tutor_profile', 'subject'
    ).order_by('-created_at')

    return render(request, 'matched_classes/student_classes.html', {'classes': classes})

@login_required
def tutor_classes(request):
    if not (request.user.profile.is_tutor or request.user.profile.is_admin_user):
        messages.error(request, 'Trang này dành cho tài khoản gia sư.')
        return redirect('home')

    classes = MatchedClass.objects.filter(tutor=request.user).select_related(
        'student', 'student__profile', 'subject'
    ).order_by('-created_at')

    return render(request, 'matched_classes/tutor_classes.html', {'classes': classes})

@login_required
def class_detail(request, pk):
    matched_class = get_object_or_404(
        MatchedClass.objects.select_related(
            'student', 'student__profile', 'tutor', 'tutor__profile', 'tutor__tutor_profile', 'subject',
            'study_request', 'class_request'
        ),
        pk=pk
    )

    # Permission check: must be student, tutor or admin
    if not (request.user == matched_class.student or request.user == matched_class.tutor or request.user.profile.is_admin_user):
        messages.error(request, 'Bạn không có quyền truy cập lớp học này.')
        return redirect('home')

    review = getattr(matched_class, 'review', None)

    return render(request, 'matched_classes/class_detail.html', {
        'matched_class': matched_class,
        'review': review,
    })

@login_required
def complete_class(request, pk):
    matched_class = get_object_or_404(MatchedClass, pk=pk)

    if not (request.user == matched_class.student or request.user == matched_class.tutor or request.user.profile.is_admin_user):
        messages.error(request, 'Bạn không có quyền cập nhật trạng thái lớp này.')
        return redirect('home')

    if request.method == 'POST':
        matched_class.status = 'completed'
        matched_class.save()
        messages.success(request, 'Đã đánh dấu lớp học hoàn thành! Học sinh có thể để lại đánh giá và chấm sao cho gia sư.')
        return redirect('matched_classes:class_detail', pk=pk)

    return redirect('matched_classes:class_detail', pk=pk)

@login_required
def cancel_class(request, pk):
    matched_class = get_object_or_404(MatchedClass, pk=pk)

    if not (request.user == matched_class.student or request.user == matched_class.tutor or request.user.profile.is_admin_user):
        messages.error(request, 'Bạn không có quyền cập nhật trạng thái lớp này.')
        return redirect('home')

    if request.method == 'POST':
        matched_class.status = 'cancelled'
        matched_class.save()
        messages.warning(request, 'Đã hủy lớp học.')
        return redirect('matched_classes:class_detail', pk=pk)

    return redirect('matched_classes:class_detail', pk=pk)
