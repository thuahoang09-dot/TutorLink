from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import ClassRequest
from .forms import ClassRequestForm
from tutors.models import Subject
from applications.models import Application

def class_list(request):
    queryset = ClassRequest.objects.filter(status='pending').select_related('student', 'student__profile', 'subject')

    q = request.GET.get('q', '').strip()
    subject_id = request.GET.get('subject')
    grade = request.GET.get('grade', '').strip()
    location = request.GET.get('location', '').strip()
    district = request.GET.get('district', '').strip()
    method = request.GET.get('method')

    if q:
        queryset = queryset.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(subject__name__icontains=q)
        )

    if subject_id:
        queryset = queryset.filter(subject_id=subject_id)

    if grade:
        queryset = queryset.filter(grade__icontains=grade)

    if location:
        if location in ['TP. Hồ Chí Minh', 'Hồ Chí Minh', 'TP.HCM', 'TP HCM']:
            queryset = queryset.filter(
                Q(location__icontains='Hồ Chí Minh') |
                Q(location__icontains='TP.HCM') |
                Q(location__icontains='HCM')
            )
        elif location in ['Hà Nội', 'HN']:
            queryset = queryset.filter(
                Q(location__icontains='Hà Nội') |
                Q(location__icontains='HN')
            )
        elif location == 'Online':
            queryset = queryset.filter(
                Q(location__icontains='Online') |
                Q(teaching_method__in=['online', 'both'])
            )
        else:
            queryset = queryset.filter(location__icontains=location)

    if district:
        queryset = queryset.filter(
            Q(location__icontains=district) |
            Q(location__icontains=district.lower()) |
            Q(location__icontains=district.title())
        )

    if method and method in ['online', 'offline', 'both']:
        if method == 'both':
            queryset = queryset.filter(teaching_method='both')
        else:
            queryset = queryset.filter(Q(teaching_method=method) | Q(teaching_method='both'))

    subjects = Subject.objects.all()

    return render(request, 'class_requests/class_list.html', {
        'class_requests': queryset,
        'subjects': subjects,
        'selected_subject': subject_id,
        'q': q,
        'grade': grade,
        'location': location,
        'district': district,
        'selected_method': method,
        'total_results': queryset.count(),
    })

def class_detail(request, pk):
    class_request = get_object_or_404(
        ClassRequest.objects.select_related('student', 'student__profile', 'subject'),
        pk=pk
    )

    has_applied = False
    my_application = None
    applications = []

    if request.user.is_authenticated:
        if request.user == class_request.student or request.user.profile.is_admin_user:
            applications = class_request.applications.select_related('tutor', 'tutor__profile', 'tutor__tutor_profile').all()
        elif request.user.profile.is_tutor:
            my_application = Application.objects.filter(class_request=class_request, tutor=request.user).first()
            if my_application:
                has_applied = True

    return render(request, 'class_requests/class_detail.html', {
        'class_request': class_request,
        'has_applied': has_applied,
        'my_application': my_application,
        'applications': applications,
    })

def get_default_timetable(schedule_str=""):
    """Tạo cấu trúc ma trận lịch tuần 2 bảng (Thứ 2 - Thứ 6 và Thứ 7 - CN) tương thích với trang hồ sơ gia sư"""
    weekdays = [('mon', 'Thứ 2'), ('tue', 'Thứ 3'), ('wed', 'Thứ 4'), ('thu', 'Thứ 5'), ('fri', 'Thứ 6')]
    weekend = [('sat', 'Thứ 7'), ('sun', 'Chủ nhật')]
    periods = [('sang', 'Sáng'), ('chieu', 'Chiều'), ('toi', 'Tối')]

    s_lower = (schedule_str or "").lower()

    def is_slot_active(d_name, p_name):
        d_map = {
            'Thứ 2': ['thứ 2', 't2'],
            'Thứ 3': ['thứ 3', 't3'],
            'Thứ 4': ['thứ 4', 't4'],
            'Thứ 5': ['thứ 5', 't5'],
            'Thứ 6': ['thứ 6', 't6'],
            'Thứ 7': ['thứ 7', 't7'],
            'Chủ nhật': ['chủ nhật', 'cn'],
        }
        tokens = d_map.get(d_name, [d_name.lower()])
        day_matched = any(t in s_lower for t in tokens)
        p_matched = p_name.lower() in s_lower
        return day_matched and p_matched

    weekday_rows = []
    for p_key, p_name in periods:
        slots = []
        for d_key, d_name in weekdays:
            slots.append({
                'day_key': d_key,
                'day_name': d_name,
                'period_key': p_key,
                'period_name': p_name,
                'is_active': is_slot_active(d_name, p_name)
            })
        weekday_rows.append({
            'period_name': p_name,
            'slots': slots
        })

    weekend_rows = []
    for p_key, p_name in periods:
        slots = []
        for d_key, d_name in weekend:
            slots.append({
                'day_key': d_key,
                'day_name': d_name,
                'period_key': p_key,
                'period_name': p_name,
                'is_active': is_slot_active(d_name, p_name)
            })
        weekend_rows.append({
            'period_name': p_name,
            'slots': slots
        })

    return {
        'weekdays': weekdays,
        'weekday_rows': weekday_rows,
        'weekend': weekend,
        'weekend_rows': weekend_rows,
    }

@login_required
def post_class(request):
    if not (request.user.profile.is_student or request.user.profile.is_admin_user):
        messages.error(request, 'Chức năng đăng bài tìm gia sư chỉ dành cho tài khoản Học sinh / Phụ huynh.')
        return redirect('class_requests:class_list')

    if request.method == 'POST':
        form = ClassRequestForm(request.POST)
        if form.is_valid():
            cr = form.save(commit=False)
            cr.student = request.user
            cr.status = 'pending'
            cr.save()
            messages.success(request, 'Đăng yêu cầu tìm gia sư thành công! Các gia sư phù hợp sẽ sớm ứng tuyển.')
            return redirect('class_requests:class_detail', pk=cr.pk)
    else:
        initial = {}
        if hasattr(request.user, 'profile') and request.user.profile.address:
            initial['location'] = request.user.profile.address
        form = ClassRequestForm(initial=initial)

    timetable = get_default_timetable()
    return render(request, 'class_requests/post_class.html', {
        'form': form,
        'timetable': timetable,
    })

@login_required
def edit_class(request, pk):
    class_request = get_object_or_404(ClassRequest, pk=pk)
    if class_request.student != request.user and not request.user.profile.is_admin_user:
        messages.error(request, 'Bạn không có quyền chỉnh sửa bài đăng này.')
        return redirect('class_requests:class_list')

    if request.method == 'POST':
        form = ClassRequestForm(request.POST, instance=class_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật bài đăng tìm gia sư thành công!')
            return redirect('class_requests:class_detail', pk=class_request.pk)
    else:
        form = ClassRequestForm(instance=class_request)

    timetable = get_default_timetable(class_request.schedule)
    return render(request, 'class_requests/post_class.html', {
        'form': form,
        'is_edit': True,
        'class_request': class_request,
        'timetable': timetable,
    })

@login_required
def delete_class(request, pk):
    class_request = get_object_or_404(ClassRequest, pk=pk)
    if class_request.student != request.user and not request.user.profile.is_admin_user:
        messages.error(request, 'Bạn không có quyền thao tác bài đăng này.')
        return redirect('class_requests:class_list')

    if request.method == 'POST':
        class_request.delete()
        messages.success(request, 'Đã xóa bài đăng tìm gia sư thành công.')
        return redirect('class_requests:my_posts')

    return redirect('class_requests:class_detail', pk=pk)

@login_required
def close_class(request, pk):
    class_request = get_object_or_404(ClassRequest, pk=pk)
    if class_request.student != request.user and not request.user.profile.is_admin_user:
        messages.error(request, 'Bạn không có quyền thao tác bài đăng này.')
        return redirect('class_requests:class_list')

    if request.method == 'POST':
        class_request.status = 'closed'
        class_request.save()
        messages.info(request, 'Đã đóng bài đăng tìm gia sư.')
        return redirect('class_requests:class_detail', pk=pk)

    return redirect('class_requests:class_detail', pk=pk)

@login_required
def my_posts(request):
    posts = ClassRequest.objects.filter(student=request.user).select_related('subject').prefetch_related('applications').order_by('-created_at')
    return render(request, 'class_requests/my_posts.html', {'posts': posts})
