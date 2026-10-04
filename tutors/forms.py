from django import forms
from .models import TutorProfile, Subject

class TutorProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Họ tên đầy đủ *',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nguyễn Thừa Hoàng'})
    )
    phone = forms.CharField(
        label='Số điện thoại *',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0334xxxxxx'})
    )
    email = forms.EmailField(
        label='Email *',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@gmail.com'})
    )
    avatar = forms.ImageField(
        label='Ảnh đại diện',
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
    )
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label='Môn học sẽ dạy *',
        required=False
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.user = user
            if hasattr(user, 'profile'):
                self.fields['full_name'].initial = user.profile.full_name
                self.fields['phone'].initial = user.profile.phone
            self.fields['email'].initial = user.email

    def clean_subjects(self):
        subjects = self.cleaned_data.get('subjects')
        if subjects and len(subjects) > 3:
            raise forms.ValidationError('Bạn chỉ được lựa chọn tối đa 3 môn dạy.')
        return subjects

    def save(self, commit=True):
        instance = super().save(commit=False)
        if hasattr(self, 'user') and self.user:
            if hasattr(self.user, 'profile'):
                full_name = self.cleaned_data.get('full_name')
                phone = self.cleaned_data.get('phone')
                if full_name:
                    self.user.profile.full_name = full_name
                if phone:
                    self.user.profile.phone = phone
                avatar = self.cleaned_data.get('avatar')
                if avatar:
                    self.user.profile.avatar = avatar
                self.user.profile.save()
            email = self.cleaned_data.get('email')
            if email:
                self.user.email = email
                self.user.save()
        if commit:
            instance.save()
            self.save_m2m()
        return instance

    class Meta:
        model = TutorProfile
        fields = [
            'gender',
            'hometown',
            'birth_date',
            'voice',
            'facebook_link',
            'location',
            'detailed_address',
            'experience',
            'achievements',
            'tutor_type',
            'university',
            'student_year',
            'major',
            'academic_level',
            'teaching_method',
            'price_per_hour',
            'subjects',
            'teaching_topics',
            'taught_classes_count',
            'available_schedule',
            'id_card_front',
            'student_card_1',
            'student_card_2',
            'student_card_3',
        ]
        widgets = {
            'gender': forms.Select(
                choices=[('', '-- Chọn giới tính --'), ('Nam', 'Nam'), ('Nữ', 'Nữ')],
                attrs={'class': 'form-select'}
            ),
            'hometown': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nghệ An, Hà Nội...'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY (VD: 14/09/2001)'}),
            'voice': forms.Select(
                choices=[('', '-- Chọn giọng nói --'), ('Miền Bắc', 'Miền Bắc'), ('Miền Nam', 'Miền Nam'), ('Miền Trung', 'Miền Trung')],
                attrs={'class': 'form-select'}
            ),
            'facebook_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vui lòng nhập link facebook chính'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hà Nội, TP.HCM...'}),
            'detailed_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số nhà, ngõ/ngách, đường, phường/xã...'}),
            
            'experience': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '- Đã có kinh nghiệm dạy học sinh khối 12 kì thi THPTQG đạt 8+...\n- Tạo nền tảng vững chắc cho học sinh mất gốc...\n- Kỹ năng truyền đạt dễ hiểu, chăm chỉ, có lộ trình ôn tập rõ ràng.'
            }),
            'achievements': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '- Đạt 26 điểm thi THPTQG khối A00...\n- Điểm thi ĐGNL ĐHQGHN đạt 112/150...\n- Đạt 12 năm học sinh giỏi liên tiếp...\n- Trúng tuyển nhiều trường đại học top đầu.'
            }),
            
            'tutor_type': forms.Select(
                choices=[
                    ('', '-- Chọn vai trò hiện tại --'),
                    ('Người đi làm', 'Người đi làm'),
                    ('Sinh viên', 'Sinh viên'),
                    ('Giáo viên', 'Giáo viên'),
                    ('Cử nhân', 'Cử nhân'),
                    ('Giảng viên', 'Giảng viên')
                ],
                attrs={'class': 'form-select'}
            ),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Trường Đại học Ngoại thương'}),
            'student_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: 3 hoặc 4'}),
            'major': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Kinh tế quốc tế, Sư phạm Toán...'}),
            'academic_level': forms.Select(
                choices=[('', '-- Chọn bậc học --'), ('Đại học', 'Đại học'), ('Thạc sĩ', 'Thạc sĩ'), ('Tiến sĩ', 'Tiến sĩ'), ('Cao đẳng', 'Cao đẳng'), ('Khác', 'Khác')],
                attrs={'class': 'form-select'}
            ),
            'teaching_method': forms.Select(
                choices=[
                    ('', '-- Chọn hình thức dạy --'),
                    ('online', 'Trực tuyến (Online)'),
                    ('offline', 'Trực tiếp (Offline)'),
                    ('both', 'Cả Online và Offline')
                ],
                attrs={'class': 'form-select'}
            ),
            'price_per_hour': forms.NumberInput(attrs={'class': 'form-control', 'step': '10000', 'placeholder': 'VD: 180000'}),
            'teaching_topics': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Toán cấp 2, Toán cấp 3, Toán cấp 1...'}),
            'taught_classes_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '7'}),
            'available_schedule': forms.HiddenInput(),
            
            'id_card_front': forms.FileInput(attrs={'class': 'form-control d-none', 'accept': 'image/*', 'onchange': 'previewUploadedImage(this, "preview-id-card")'}),
            'student_card_1': forms.FileInput(attrs={'class': 'form-control d-none', 'accept': 'image/*', 'onchange': 'previewUploadedImage(this, "preview-student-card-1")'}),
            'student_card_2': forms.FileInput(attrs={'class': 'form-control d-none', 'accept': 'image/*', 'onchange': 'previewUploadedImage(this, "preview-student-card-2")'}),
            'student_card_3': forms.FileInput(attrs={'class': 'form-control d-none', 'accept': 'image/*', 'onchange': 'previewUploadedImage(this, "preview-student-card-3")'}),
        }

