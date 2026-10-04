from .models import UserProfile
import json
from config.constants import VIETNAM_PROVINCES, POPULAR_CITIES, VIETNAM_DISTRICTS

def get_subject_groups():
    try:
        from tutors.models import Subject
        return [
            {
                'name': 'Môn phổ thông',
                'category': 'pho_thong',
                'subjects': list(Subject.objects.filter(category='pho_thong').order_by('order', 'id')),
            },
            {
                'name': 'Môn ngoại ngữ',
                'category': 'ngoai_ngu',
                'subjects': list(Subject.objects.filter(category='ngoai_ngu').order_by('order', 'id')),
            },
            {
                'name': 'Thể thao & Nghệ thuật',
                'category': 'the_thao_nghe_thuat',
                'subjects': list(Subject.objects.filter(category='the_thao_nghe_thuat').order_by('order', 'id')),
            },
        ]
    except Exception:
        return []

def user_profile_context(request):
    """Context processor to provide easy access to user profile, pending badges, and common data."""
    context = {
        'user_profile': None,
        'unread_notifications_count': 0,
        'recent_notifications': [],
        'unread_study_requests_count': 0,
        'pending_applications_count': 0,
        'pending_tutor_approvals_count': 0,
        'vietnam_provinces': VIETNAM_PROVINCES,
        'popular_cities': POPULAR_CITIES,
        'subject_groups': get_subject_groups(),
        'vietnam_districts_json': json.dumps(VIETNAM_DISTRICTS, ensure_ascii=False),
    }
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            context['user_profile'] = profile

            # Facebook Notifications
            from .models import Notification
            context['unread_notifications_count'] = Notification.objects.filter(
                recipient=request.user, is_read=False
            ).count()
            context['recent_notifications'] = list(
                Notification.objects.filter(recipient=request.user)
                .select_related('sender', 'sender__profile')[:10]
            )
            
            # Badge counts for quick navigation
            if profile.is_tutor:
                from study_requests.models import StudyRequest
                context['unread_study_requests_count'] = StudyRequest.objects.filter(
                    tutor=request.user, status='pending'
                ).count()
            elif profile.is_student:
                from applications.models import Application
                context['pending_applications_count'] = Application.objects.filter(
                    class_request__student=request.user, status='pending'
                ).count()
            elif profile.is_admin_user:
                from tutors.models import TutorProfile
                context['pending_tutor_approvals_count'] = TutorProfile.objects.filter(
                    approval_status='pending'
                ).count()
        except Exception:
            pass
    return context
