from django.db import models
from django.contrib.auth.models import User
from tutors.models import Subject

class StudyRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ gia sư phản hồi'),
        ('accepted', 'Đã đồng ý'),
        ('rejected', 'Đã từ chối'),
    ]

    TEACHING_METHOD_CHOICES = [
        ('online', 'Trực tuyến (Online)'),
        ('offline', 'Trực tiếp (Offline)'),
        ('both', 'Linh hoạt'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_study_requests')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_study_requests')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='study_requests')
    grade = models.CharField('Khối lớp / Trình độ', max_length=50, default='Lớp 10')
    location = models.CharField('Địa chỉ / Khu vực học', max_length=255, blank=True, default='')
    sessions_per_week = models.CharField('Số buổi / tuần', max_length=50, default='2-3 buổi/tuần', blank=True)
    schedule = models.CharField('Thời gian có thể học', max_length=200)
    teaching_method = models.CharField('Hình thức học', max_length=20, choices=TEACHING_METHOD_CHOICES, default='both')
    note = models.TextField('Ghi chú / Mục tiêu học tập', blank=True)
    status = models.CharField('Trạng thái', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Yêu cầu học trực tiếp'
        verbose_name_plural = 'Danh sách Yêu cầu học trực tiếp'
        ordering = ['-created_at']

    def __str__(self):
        return f"Yêu cầu từ {self.student.username} gửi tới {self.tutor.username} ({self.subject.name})"
