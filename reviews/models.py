from django.db import models
from django.contrib.auth.models import User
from matched_classes.models import MatchedClass

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 sao - Kém'),
        (2, '2 sao - Trung bình'),
        (3, '3 sao - Khá'),
        (4, '4 sao - Tốt'),
        (5, '5 sao - Xuất sắc'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_reviews')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_reviews')
    matched_class = models.OneToOneField(MatchedClass, on_delete=models.CASCADE, related_name='review')
    rating = models.IntegerField('Đánh giá sao', choices=RATING_CHOICES, default=5)
    comment = models.TextField('Nhận xét về gia sư')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Đánh giá gia sư'
        verbose_name_plural = 'Danh sách Đánh giá'
        ordering = ['-created_at']

    def __str__(self):
        return f"Đánh giá {self.rating} sao từ {self.student.username} cho {self.tutor.username}"

    def star_range(self):
        return range(self.rating)

    def empty_star_range(self):
        return range(5 - self.rating)
