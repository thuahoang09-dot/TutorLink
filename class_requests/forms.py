from django import forms
from .models import ClassRequest
from tutors.models import Subject

class ClassRequestForm(forms.ModelForm):
    location = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

    SESSION_CHOICES = [
        ('1 buổi/tuần', '1 buổi / tuần'),
        ('2 buổi/tuần', '2 buổi / tuần'),
        ('3 buổi/tuần', '3 buổi / tuần'),
        ('4 buổi/tuần', '4 buổi / tuần'),
        ('5 buổi/tuần', '5 buổi / tuần'),
        ('Linh hoạt / Thỏa thuận', 'Linh hoạt / Thỏa thuận'),
    ]
    sessions_per_week = forms.ChoiceField(
        choices=SESSION_CHOICES,
        initial='3 buổi/tuần',
        widget=forms.Select(attrs={'class': 'form-select fw-semibold text-primary'})
    )

    class Meta:
        model = ClassRequest
        fields = [
            'title',
            'subject',
            'grade',
            'location',
            'budget',
            'budget_type',
            'sessions_per_week',
            'schedule',
            'teaching_method',
            'description',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Tìm gia sư Toán lớp 10 ôn thi học kỳ tại Cầu Giấy'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Lớp 10, Lớp 12, Đại học...'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'step': '10000', 'placeholder': '200000'}),
            'budget_type': forms.Select(attrs={'class': 'form-select'}),
            'schedule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Tối thứ 2, 4, 6 từ 19h30 - 21h30'}),
            'teaching_method': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mô tả học lực hiện tại của học sinh, mục tiêu cần đạt, yêu cầu cụ thể đối với gia sư...'}),
        }

    def clean_location(self):
        location = self.cleaned_data.get('location', '').strip()
        if not location:
            province = self.data.get('post_province', '').strip()
            district = self.data.get('post_district', '').strip()
            specific = self.data.get('post_specific_address', '').strip()
            if province == 'Online':
                location = 'Học Online'
            else:
                parts = [p for p in [specific, district, province] if p]
                if parts:
                    location = ', '.join(parts)
        if not location:
            raise forms.ValidationError('Vui lòng chọn Tỉnh/Thành phố hoặc địa chỉ học.')
        return location


