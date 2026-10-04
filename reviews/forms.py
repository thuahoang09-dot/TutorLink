from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Chia sẻ cảm nhận của bạn về sự nhiệt tình, đúng giờ, phương pháp giảng dạy và hiệu quả học tập với gia sư...'}),
        }
        labels = {
            'rating': 'Mức điểm đánh giá (1 - 5 sao)',
            'comment': 'Nội dung nhận xét',
        }
