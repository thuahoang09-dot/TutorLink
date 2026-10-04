from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserProfileForm
from .models import UserProfile
from tutors.models import TutorProfile

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    initial_role = request.GET.get('role', 'student')
    if initial_role not in ['student', 'tutor']:
        initial_role = 'student'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            full_name = form.cleaned_data['full_name']
            phone = form.cleaned_data.get('phone', '')

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=full_name
            )

            # Profile is auto-created by signal, let's update role and fields
            profile = user.profile
            profile.role = role
            profile.full_name = full_name
            profile.phone = phone
            profile.save()

            # If tutor, create empty TutorProfile so user can fill it themselves
            if role == 'tutor':
                TutorProfile.objects.get_or_create(
                    user=user,
                    defaults={
                        'introduction': '',
                        'approval_status': 'pending'
                    }
                )

            messages.success(request, f'Đăng ký tài khoản thành công! Bạn có thể đăng nhập ngay.')
            return redirect('accounts:login')
    else:
        form = RegisterForm(initial={'role': initial_role})

    return render(request, 'accounts/register.html', {'form': form, 'selected_role': initial_role})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if account is locked
            if hasattr(user, 'profile') and user.profile.is_locked:
                messages.error(request, 'Tài khoản của bạn đã bị khóa do vi phạm chính sách. Vui lòng liên hệ Quản trị viên.')
                return render(request, 'accounts/login.html')

            login(request, user)
            messages.success(request, f'Chào mừng {user.profile.full_name or user.username} đã quay trở lại!')

            # Role-based redirection
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            if user.profile.is_admin_user:
                return redirect('dashboard:admin_dashboard')
            elif user.profile.is_tutor:
                return redirect('dashboard:tutor_dashboard')
            else:
                return redirect('dashboard:student_dashboard')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác!')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Bạn đã đăng xuất thành công.')
    return redirect('home')

import os
from django.http import JsonResponse

@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        email = request.POST.get('email', '').strip()
        if form.is_valid():
            if email:
                request.user.email = email
                request.user.save()
            form.save()
            messages.success(request, 'Cập nhật hồ sơ cá nhân thành công!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'form': form,
        'profile': profile
    })

@login_required
def update_avatar_view(request):
    """API cập nhật ảnh đại diện chuẩn phong cách Facebook qua AJAX"""
    if request.method == 'POST':
        profile = request.user.profile
        avatar_file = request.FILES.get('avatar')
        if not avatar_file:
            return JsonResponse({'success': False, 'message': 'Không tìm thấy file ảnh tải lên.'}, status=400)

        # Validate file size (max 5MB)
        if avatar_file.size > 5 * 1024 * 1024:
            return JsonResponse({'success': False, 'message': 'Dung lượng ảnh vượt quá 5MB. Vui lòng chọn ảnh nhẹ hơn.'}, status=400)

        # Xóa file ảnh cũ nếu có
        if profile.avatar:
            try:
                if os.path.isfile(profile.avatar.path):
                    os.remove(profile.avatar.path)
            except Exception:
                pass

        profile.avatar = avatar_file
        profile.save()

        return JsonResponse({
            'success': True,
            'message': 'Cập nhật ảnh đại diện thành công!',
            'avatar_url': profile.get_avatar_url()
        })
    return JsonResponse({'success': False, 'message': 'Phương thức không hợp lệ.'}, status=405)

@login_required
def delete_avatar_view(request):
    """API gỡ ảnh đại diện quay về mặc định"""
    if request.method == 'POST':
        profile = request.user.profile
        if profile.avatar:
            try:
                if os.path.isfile(profile.avatar.path):
                    os.remove(profile.avatar.path)
            except Exception:
                pass
            profile.avatar = None
            profile.save()

        return JsonResponse({
            'success': True,
            'message': 'Đã đặt lại ảnh đại diện mặc định!',
            'avatar_url': profile.get_avatar_url()
        })
    return JsonResponse({'success': False, 'message': 'Phương thức không hợp lệ.'}, status=405)

from .models import Notification

@login_required
def mark_notification_read(request, notification_id):
    """Đánh dấu một thông báo là đã đọc và chuyển hướng đến trang đích"""
    notification = get_object_or_404(Notification, pk=notification_id, recipient=request.user)
    notification.is_read = True
    notification.save()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('ajax'):
        return JsonResponse({'success': True, 'unread_count': request.user.notifications.filter(is_read=False).count()})

    if notification.link:
        return redirect(notification.link)
    return redirect('home')

@login_required
def mark_all_notifications_read(request):
    """Đánh dấu tất cả thông báo của người dùng là đã đọc"""
    request.user.notifications.filter(is_read=False).update(is_read=True)
    return JsonResponse({'success': True, 'unread_count': 0})

@login_required
def get_notifications_api(request):
    """API lấy danh sách thông báo và số lượng chưa đọc mới nhất chuẩn Facebook"""
    unread_count = request.user.notifications.filter(is_read=False).count()
    notifs = request.user.notifications.select_related('sender', 'sender__profile')[:15]

    data = []
    for n in notifs:
        badge = n.get_badge_icon()
        data.append({
            'id': n.id,
            'title': n.title,
            'message': n.message,
            'link': n.link,
            'is_read': n.is_read,
            'time_ago': n.get_time_ago(),
            'avatar_url': n.get_sender_avatar(),
            'badge_icon': badge['icon'],
            'badge_bg': badge['bg'],
        })
    return JsonResponse({
        'success': True,
        'unread_count': unread_count,
        'notifications': data
    })


