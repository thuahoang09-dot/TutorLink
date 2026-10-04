from django.db import models
from django.contrib.auth.models import User
from tutors.models import Subject

class ClassRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Đang tìm gia sư'),
        ('accepted', 'Đã ghép lớp'),
        ('closed', 'Đã đóng bài'),
        ('cancelled', 'Đã hủy'),
    ]

    TEACHING_METHOD_CHOICES = [
        ('online', 'Trực tuyến (Online)'),
        ('offline', 'Trực tiếp (Offline)'),
        ('both', 'Linh hoạt Online/Offline'),
    ]

    BUDGET_TYPE_CHOICES = [
        ('per_session', 'VNĐ / Buổi'),
        ('per_hour', 'VNĐ / Giờ'),
        ('per_month', 'VNĐ / Tháng'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_requests')
    title = models.CharField('Tiêu đề bài đăng', max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='class_requests')
    grade = models.CharField('Khối lớp / Trình độ', max_length=50, default='Lớp 10')
    location = models.CharField('Khu vực học', max_length=150, default='Hà Nội')
    budget = models.IntegerField('Mức thù lao dự kiến', default=200000)
    budget_type = models.CharField('Đơn vị ngân sách', max_length=20, choices=BUDGET_TYPE_CHOICES, default='per_session')
    sessions_per_week = models.CharField('Số buổi / tuần', max_length=50, default='2-3 buổi/tuần', blank=True)
    schedule = models.CharField('Thời gian có thể học', max_length=200)
    teaching_method = models.CharField('Hình thức học', max_length=20, choices=TEACHING_METHOD_CHOICES, default='both')
    description = models.TextField('Mô tả chi tiết yêu cầu')
    status = models.CharField('Trạng thái', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Yêu cầu tìm gia sư'
        verbose_name_plural = 'Danh sách yêu cầu tìm gia sư'
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.subject}] {self.title} - {self.student.username}"

    @property
    def applications_count(self):
        return self.applications.count()

    @property
    def is_open(self):
        return self.status == 'pending'
