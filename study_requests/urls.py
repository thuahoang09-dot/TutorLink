from django.urls import path
from . import views

app_name = 'study_requests'

urlpatterns = [
    path('create/<int:tutor_id>/', views.create_request, name='create_request'),
    path('tutor-requests/', views.tutor_requests, name='tutor_requests'),
    path('student-requests/', views.student_requests, name='student_requests'),
    path('accept/<int:request_id>/', views.accept_request, name='accept_request'),
    path('reject/<int:request_id>/', views.reject_request, name='reject_request'),
]
