from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Học sinh'),
        ('tutor', 'Gia sư'),
        ('admin', 'Quản trị viên'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    full_name = models.CharField('Họ và tên', max_length=150, blank=True)
    phone = models.CharField('Số điện thoại', max_length=20, blank=True)
    address = models.CharField('Địa chỉ', max_length=255, blank=True)
    avatar = models.ImageField('Ảnh đại diện', upload_to='avatars/', null=True, blank=True)
    bio = models.TextField('Giới thiệu ngắn', blank=True)
    is_locked = models.BooleanField('Đang bị khóa', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name or self.user.username} ({self.get_role_display()})"

    @property
    def is_student(self):
        return self.role == 'student'

    @property
    def is_tutor(self):
        return self.role == 'tutor'

    @property
    def is_admin_user(self):
        return self.role == 'admin' or self.user.is_superuser or self.user.is_staff

    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        # Default avatar using initials or UI Avatars service
        name = self.full_name or self.user.username
        return f"https://ui-avatars.com/api/?name={name}&background=2563eb&color=fff&size=128"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if kwargs.get('raw'):
        return

    if created:
        role = 'admin' if (instance.is_superuser or instance.is_staff) else 'student'
        UserProfile.objects.create(
            user=instance,
            role=role,
            full_name=instance.get_full_name() or ''
        )
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()

from django.utils import timezone

class Notification(models.Model):
    TYPE_CHOICES = [
        ('apply_class', 'Gia sư nhận lớp / ứng tuyển'),
        ('accept_application', 'Học sinh nhận gia sư'),
        ('reject_application', 'Đơn ứng tuyển bị từ chối'),
        ('study_request', 'Yêu cầu học từ học sinh'),
        ('accept_request', 'Gia sư nhận yêu cầu học'),
        ('reject_request', 'Gia sư từ chối yêu cầu'),
        ('review', 'Đánh giá nhận xét'),
        ('system', 'Hệ thống'),
    ]

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_notifications')
    notification_type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='system')
    title = models.CharField(max_length=255)
    message = models.TextField()
    link = models.CharField(max_length=255, blank=True, default='')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Thông báo tới {self.recipient.username}: {self.title}"

    def get_time_ago(self):
        now = timezone.now()
        diff = now - self.created_at
        seconds = diff.total_seconds()
        if seconds < 60:
            return "Vừa xong"
        elif seconds < 3600:
            minutes = int(seconds // 60)
            return f"{minutes} phút trước"
        elif seconds < 86400:
            hours = int(seconds // 3600)
            return f"{hours} giờ trước"
        elif seconds < 604800:
            days = int(seconds // 86400)
            return f"{days} ngày trước"
        else:
            return self.created_at.strftime("%d/%m/%Y")

    def get_sender_avatar(self):
        if self.sender and hasattr(self.sender, 'profile'):
            return self.sender.profile.get_avatar_url()
        return "https://ui-avatars.com/api/?name=TutorLink&background=1877F2&color=fff&size=64"

    def get_badge_icon(self):
        mapping = {
            'apply_class': {'icon': 'bi-briefcase-fill', 'bg': 'bg-primary'},
            'accept_application': {'icon': 'bi-mortarboard-fill', 'bg': 'bg-success'},
            'reject_application': {'icon': 'bi-x-circle-fill', 'bg': 'bg-secondary'},
            'study_request': {'icon': 'bi-person-plus-fill', 'bg': 'bg-primary'},
            'accept_request': {'icon': 'bi-check-circle-fill', 'bg': 'bg-success'},
            'reject_request': {'icon': 'bi-dash-circle-fill', 'bg': 'bg-danger'},
            'review': {'icon': 'bi-star-fill', 'bg': 'bg-warning text-dark'},
            'system': {'icon': 'bi-bell-fill', 'bg': 'bg-info'},
        }
        return mapping.get(self.notification_type, {'icon': 'bi-bell-fill', 'bg': 'bg-primary'})

def create_notification(recipient, title, message, link='', sender=None, notification_type='system'):
    if not recipient:
        return None
    return Notification.objects.create(
        recipient=recipient,
        sender=sender,
        notification_type=notification_type,
        title=title,
        message=message,
        link=link
    )

