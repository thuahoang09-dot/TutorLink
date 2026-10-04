from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from matched_classes.models import MatchedClass

@login_required
def create_review(request, matched_class_id):
    matched_class = get_object_or_404(
        MatchedClass.objects.select_related('student', 'tutor', 'tutor__profile', 'subject'),
        pk=matched_class_id
    )

    # Only the student in this class can write review
    if matched_class.student != request.user and not request.user.profile.is_admin_user:
        messages.error(request, 'Chỉ có học sinh tham gia lớp này mới có quyền đánh giá.')
        return redirect('matched_classes:class_detail', pk=matched_class_id)

    # Check if review already exists
    if hasattr(matched_class, 'review'):
        messages.info(request, 'Lớp học này đã được đánh giá rồi.')
        return redirect('matched_classes:class_detail', pk=matched_class_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user
            review.tutor = matched_class.tutor
            review.matched_class = matched_class
            review.save()
            messages.success(request, 'Cảm ơn bạn đã gửi đánh giá cho gia sư!')
            return redirect('matched_classes:class_detail', pk=matched_class_id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/create_review.html', {
        'form': form,
        'matched_class': matched_class,
    })
