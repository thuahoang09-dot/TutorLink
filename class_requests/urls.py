from django.urls import path
from . import views

app_name = 'class_requests'

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('<int:pk>/', views.class_detail, name='class_detail'),
    path('post/', views.post_class, name='post_class'),
    path('<int:pk>/edit/', views.edit_class, name='edit_class'),
    path('<int:pk>/delete/', views.delete_class, name='delete_class'),
    path('<int:pk>/close/', views.close_class, name='close_class'),
    path('my-posts/', views.my_posts, name='my_posts'),
]
