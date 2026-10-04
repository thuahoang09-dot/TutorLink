from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView
from config.views import home_view, assistant_chat_api, view_project_pdf
from accounts import views as account_views
from tutors import views as tutor_views
from class_requests import views as class_views
from applications import views as app_views
from study_requests import views as study_views
from matched_classes import views as match_views
from dashboard import views as dash_views

urlpatterns = [
    # General Routes (README Section 8)
    path('', home_view, name='home'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
    path('pdf/', view_project_pdf, name='project_pdf'),
    path('README.pdf', view_project_pdf, name='readme_pdf'),
    path('api/assistant/chat/', assistant_chat_api, name='assistant_chat_api'),
    path('login/', account_views.login_view, name='login'),
    path('register/', account_views.register_view, name='register'),
    path('profile/', account_views.profile_view, name='profile'),

    # Student direct convenience URLs (README Section 8)
    path('student/dashboard/', dash_views.student_dashboard, name='student_dashboard'),
    path('student/post-class/', class_views.post_class, name='student_post_class'),
    path('student/posts/', class_views.my_posts, name='student_posts'),
    path('student/requests/', study_views.student_requests, name='student_requests'),
    path('student/classes/', match_views.student_classes, name='student_classes'),

    # Tutor direct convenience URLs (README Section 8)
    path('tutor/dashboard/', dash_views.tutor_dashboard, name='tutor_dashboard'),
    path('tutor/profile/', tutor_views.edit_tutor_profile, name='tutor_profile'),
    path('tutor/applications/', app_views.my_applications, name='tutor_applications'),
    path('tutor/requests/', study_views.tutor_requests, name='tutor_requests'),
    path('tutor/classes/', match_views.tutor_classes, name='tutor_classes'),

    # Modular App URLs
    path('accounts/', include('accounts.urls')),
    path('tutors/', include('tutors.urls')),
    path('classes/', include('class_requests.urls')),
    path('applications/', include('applications.urls')),
    path('study-requests/', include('study_requests.urls')),
    path('matched-classes/', include('matched_classes.urls')),
    path('reviews/', include('reviews.urls')),
    path('', include('dashboard.urls')),

    # Django Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
