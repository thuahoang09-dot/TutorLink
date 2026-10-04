from django.db import models
from django.contrib.auth.models import User
from class_requests.models import ClassRequest

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ học sinh phản hồi'),
        ('accepted', 'Được chấp nhận'),
        ('rejected', 'Bị từ chối'),
    ]

    class_request = models.ForeignKey(ClassRequest, on_delete=models.CASCADE, related_name='applications')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_applications')
    message = models.TextField('Lời nhắn / Giới thiệu bản thân')
    proposed_price = models.IntegerField('Học phí đề xuất (VNĐ)', null=True, blank=True)
    status = models.CharField('Trạng thái', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Đơn ứng tuyển'
        verbose_name_plural = 'Danh sách Đơn ứng tuyển'
        unique_together = ('class_request', 'tutor')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.tutor.username} ứng tuyển: {self.class_request.title}"
