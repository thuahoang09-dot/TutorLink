from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Student & Tutor Dashboards
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('tutor/dashboard/', views.tutor_dashboard, name='tutor_dashboard'),

    # Admin Dashboard & Submodules (Specified in README Section 8)
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/users/', views.admin_users, name='admin_users'),
    path('admin-dashboard/users/<int:user_id>/toggle-lock/', views.admin_toggle_lock, name='admin_toggle_lock'),
    path('admin-dashboard/tutors/', views.admin_tutors, name='admin_tutors'),
    path('admin-dashboard/tutors/<int:tutor_id>/approve/', views.admin_approve_tutor, name='admin_approve_tutor'),
    path('admin-dashboard/posts/', views.admin_posts, name='admin_posts'),
    path('admin-dashboard/classes/', views.admin_classes, name='admin_classes'),
    path('admin-dashboard/reviews/', views.admin_reviews, name='admin_reviews'),
    path('admin-dashboard/reviews/<int:review_id>/delete/', views.admin_delete_review, name='admin_delete_review'),
    path('admin-dashboard/statistics/', views.admin_statistics, name='admin_statistics'),
]
