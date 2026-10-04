from django import forms
from .models import StudyRequest
from tutors.models import Subject

class StudyRequestForm(forms.ModelForm):
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
        model = StudyRequest
        fields = ['subject', 'grade', 'location', 'teaching_method', 'sessions_per_week', 'schedule', 'note']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Lớp 11, Ôn thi Đại học...'}),
            'schedule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Tối thứ 2, 4, 6 từ 19h30 - 21h30'}),
            'teaching_method': forms.Select(attrs={'class': 'form-select'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ghi chú về học lực hiện tại, mục tiêu điểm số, yêu cầu chi tiết đối với gia sư...'}),
        }

    def __init__(self, *args, tutor=None, **kwargs):
        super().__init__(*args, **kwargs)
        if tutor and hasattr(tutor, 'tutor_profile'):
            # Filter subjects to those taught by the tutor if available
            tutor_subjects = tutor.tutor_profile.subjects.all()
            if tutor_subjects.exists():
                self.fields['subject'].queryset = tutor_subjects

    def clean_location(self):
        location = self.cleaned_data.get('location', '').strip()
        teaching_method = self.data.get('teaching_method', '')
        province = self.data.get('post_province', '').strip()
        district = self.data.get('post_district', '').strip()
        specific = self.data.get('post_specific_address', '').strip()

        if province == 'Online' or teaching_method == 'online':
            return 'Học Online'

        if not location:
            parts = [p for p in [specific, district, province] if p]
            if parts:
                location = ', '.join(parts)

        if teaching_method == 'offline' and not location:
            raise forms.ValidationError('Vui lòng chọn Tỉnh/Thành phố hoặc địa chỉ học khi học Trực tiếp (Offline).')

        return location

