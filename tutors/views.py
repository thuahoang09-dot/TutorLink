from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import TutorProfile, Subject, TutorCertificate
from .forms import TutorProfileForm
from reviews.models import Review

def tutor_list(request):
    # Only show approved tutors to public
    queryset = TutorProfile.objects.filter(approval_status='approved').select_related('user', 'user__profile').prefetch_related('subjects')

    q = request.GET.get('q', '').strip()
    subject_id = request.GET.get('subject')
    location = request.GET.get('location', '').strip()
    district = request.GET.get('district', '').strip()
    method = request.GET.get('method')
    price_max = request.GET.get('price_max')

    if q:
        queryset = queryset.filter(
            Q(user__profile__full_name__icontains=q) |
            Q(user__username__icontains=q) |
            Q(introduction__icontains=q) |
            Q(education__icontains=q) |
            Q(subjects__name__icontains=q)
        ).distinct()

    if subject_id:
        queryset = queryset.filter(subjects__id=subject_id)

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

    if price_max:
        if price_max in ['above_500000', 'over_500000', '500000_plus', '>500000']:
            queryset = queryset.filter(price_per_hour__gte=500000)
        else:
            try:
                queryset = queryset.filter(price_per_hour__lte=int(price_max))
            except ValueError:
                pass

    subjects = Subject.objects.all()

    return render(request, 'tutors/tutor_list.html', {
        'tutors': queryset,
        'subjects': subjects,
        'selected_subject': subject_id,
        'q': q,
        'location': location,
        'district': district,
        'selected_method': method,
        'price_max': price_max,
        'total_results': queryset.count(),
    })

def tutor_detail(request, pk):
    tutor = get_object_or_404(TutorProfile.objects.select_related('user', 'user__profile').prefetch_related('subjects'), pk=pk)
    
    # Check permission: if not approved, allow tutor himself, admin, or students who received an application
    if tutor.approval_status != 'approved':
        from applications.models import Application
        from study_requests.models import StudyRequest
        is_relevant_student = request.user.is_authenticated and (
            Application.objects.filter(class_request__student=request.user, tutor=tutor.user).exists() or
            StudyRequest.objects.filter(student=request.user, tutor=tutor.user).exists()
        )
        if not (request.user.is_authenticated and (request.user == tutor.user or request.user.profile.is_admin_user or is_relevant_student)):
            messages.warning(request, 'Hồ sơ gia sư này đang trong quá trình kiểm duyệt hoặc đã bị ẩn.')
            return redirect('tutors:tutor_list')

    reviews = Review.objects.filter(tutor=tutor.user).select_related('student', 'student__profile').order_by('-created_at')

    return render(request, 'tutors/tutor_detail.html', {
        'tutor': tutor,
        'reviews': reviews,
    })

@login_required
def edit_tutor_profile(request):
    if not request.user.profile.is_tutor:
        messages.error(request, 'Chức năng này chỉ dành cho tài khoản gia sư.')
        return redirect('home')

    tutor_profile, created = TutorProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'delete_cert_id' in request.POST:
            cert_id = request.POST.get('delete_cert_id')
            TutorCertificate.objects.filter(id=cert_id, tutor=tutor_profile).delete()
            messages.success(request, 'Đã xóa tệp minh chứng!')
            return redirect('tutors:edit_tutor_profile')

        form = TutorProfileForm(request.POST, request.FILES, instance=tutor_profile, user=request.user)
        if form.is_valid():
            profile_instance = form.save(commit=False)
            if profile_instance.approval_status == 'rejected':
                profile_instance.approval_status = 'pending'
            profile_instance.save()
            form.save_m2m()
            # Handle multiple certificate files
            uploaded_files = request.FILES.getlist('certificate_files')
            for f in uploaded_files:
                TutorCertificate.objects.create(tutor=tutor_profile, file=f, title=f.name)
            messages.success(request, 'Cập nhật hồ sơ gia sư thành công! Hồ sơ sẽ được chuyển tới Ban Quản Trị xem xét.')
            return redirect('tutors:edit_tutor_profile')
    else:
        form = TutorProfileForm(instance=tutor_profile, user=request.user)

    pho_thong_subjects = Subject.objects.filter(category='pho_thong').order_by('order', 'name')
    ngoai_ngu_subjects = Subject.objects.filter(category='ngoai_ngu').order_by('order', 'name')
    the_thao_subjects = Subject.objects.filter(category='the_thao_nghe_thuat').order_by('order', 'name')
    selected_subject_ids = list(tutor_profile.subjects.values_list('id', flat=True))
    certificates = tutor_profile.certificates.all()

    return render(request, 'tutors/edit_profile.html', {
        'form': form,
        'tutor_profile': tutor_profile,
        'certificates': certificates,
        'pho_thong_subjects': pho_thong_subjects,
        'ngoai_ngu_subjects': ngoai_ngu_subjects,
        'the_thao_subjects': the_thao_subjects,
        'selected_subject_ids': selected_subject_ids,
        'timetable': tutor_profile.get_split_timetable(),
    })

