from django.urls import path
from . import views

app_name = 'matched_classes'

urlpatterns = [
    path('student/', views.student_classes, name='student_classes'),
    path('tutor/', views.tutor_classes, name='tutor_classes'),
    path('<int:pk>/', views.class_detail, name='class_detail'),
    path('<int:pk>/complete/', views.complete_class, name='complete_class'),
    path('<int:pk>/cancel/', views.cancel_class, name='cancel_class'),
]
