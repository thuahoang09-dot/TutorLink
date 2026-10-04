from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:class_id>/', views.apply_class, name='apply_class'),
    path('accept/<int:application_id>/', views.accept_application, name='accept_application'),
    path('reject/<int:application_id>/', views.reject_application, name='reject_application'),
    path('my-applications/', views.my_applications, name='my_applications'),
]
