from django.db import models
from django.contrib.auth.models import User
from tutors.models import Subject
from class_requests.models import ClassRequest
from study_requests.models import StudyRequest

class MatchedClass(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'Đang học'),
        ('completed', 'Đã hoàn thành'),
        ('cancelled', 'Đã hủy'),
    ]

    TEACHING_METHOD_CHOICES = [
        ('online', 'Trực tuyến (Online)'),
        ('offline', 'Trực tiếp (Offline)'),
        ('both', 'Linh hoạt'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_matched_classes')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_matched_classes')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='matched_classes')
    class_request = models.ForeignKey(ClassRequest, on_delete=models.SET_NULL, null=True, blank=True, related_name='matched_classes')
    study_request = models.ForeignKey(StudyRequest, on_delete=models.SET_NULL, null=True, blank=True, related_name='matched_classes')
    start_date = models.DateField('Ngày bắt đầu', auto_now_add=True)
    schedule = models.CharField('Lịch học', max_length=200, blank=True)
    hourly_rate = models.IntegerField('Học phí thỏa thuận (VNĐ)', default=150000)
    teaching_method = models.CharField('Hình thức', max_length=20, choices=TEACHING_METHOD_CHOICES, default='both')
    status = models.CharField('Trạng thái lớp', max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Lớp đã ghép'
        verbose_name_plural = 'Danh sách Lớp đã ghép'
        ordering = ['-created_at']

    def __str__(self):
        return f"Lớp {self.subject.name}: {self.student.username} - {self.tutor.username} ({self.get_status_display()})"

    @property
    def has_review(self):
        return hasattr(self, 'review')

    @property
    def grade(self):
        if self.study_request and self.study_request.grade:
            return self.study_request.grade
        if self.class_request and self.class_request.grade:
            return self.class_request.grade
        return None

    @property
    def location(self):
        if self.study_request and self.study_request.location:
            return self.study_request.location
        if self.class_request and self.class_request.location:
            return self.class_request.location
        return None

    @property
    def request_note(self):
        if self.study_request and self.study_request.note:
            return self.study_request.note
        if self.class_request and self.class_request.description:
            return self.class_request.description
        return None

    @property
    def sessions_per_week(self):
        if self.study_request and getattr(self.study_request, 'sessions_per_week', None):
            return self.study_request.sessions_per_week
        if self.class_request and getattr(self.class_request, 'sessions_per_week', None):
            return self.class_request.sessions_per_week
        return None

