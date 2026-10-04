from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Subject(models.Model):
    CATEGORY_CHOICES = [
        ('pho_thong', 'Môn phổ thông'),
        ('ngoai_ngu', 'Môn ngoại ngữ'),
        ('the_thao_nghe_thuat', 'Thể thao & Nghệ thuật'),
    ]

    name = models.CharField('Tên môn học', max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    category = models.CharField('Nhóm môn học', max_length=50, choices=CATEGORY_CHOICES, default='pho_thong')
    icon = models.CharField('Icon Bootstrap', max_length=50, default='bi-book')
    description = models.TextField('Mô tả môn học', blank=True)
    order = models.IntegerField('Thứ tự hiển thị', default=0)

    class Meta:
        verbose_name = 'Môn học'
        verbose_name_plural = 'Danh sách Môn học'
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return self.name

class TutorProfile(models.Model):
    TEACHING_METHOD_CHOICES = [
        ('online', 'Trực tuyến (Online)'),
        ('offline', 'Trực tiếp (Offline)'),
        ('both', 'Cả Online và Offline'),
    ]

    APPROVAL_STATUS_CHOICES = [
        ('pending', 'Chờ duyệt'),
        ('approved', 'Đã duyệt'),
        ('rejected', 'Bị từ chối'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    subjects = models.ManyToManyField(Subject, related_name='tutors', blank=True)
    introduction = models.TextField('Giới thiệu bản thân', blank=True)
    experience = models.TextField('Kinh nghiệm giảng dạy', blank=True)
    education = models.TextField('Học vấn & Bằng cấp', blank=True)
    certificate_file = models.FileField(
        'Tệp minh chứng (Ảnh / PDF bằng cấp, chứng chỉ)',
        upload_to='certificates/',
        blank=True,
        null=True
    )
    certificate_link = models.URLField(
        'Link minh chứng (Google Drive / OneDrive / Portfolio)',
        max_length=500,
        blank=True,
        null=True
    )
    price_per_hour = models.IntegerField('Học phí / giờ (VNĐ)', null=True, blank=True, default=None)
    location = models.CharField('Khu vực dạy', max_length=150, blank=True, default='')
    teaching_method = models.CharField(
        'Hình thức dạy',
        max_length=20,
        choices=TEACHING_METHOD_CHOICES,
        blank=True,
        default=''
    )
    approval_status = models.CharField(
        'Trạng thái phê duyệt',
        max_length=20,
        choices=APPROVAL_STATUS_CHOICES,
        default='pending'
    )
    admin_feedback = models.TextField('Nhận xét của Admin', blank=True)

    # Các trường thông tin chi tiết chuẩn trung tâm gia sư chuyên nghiệp
    birth_year = models.IntegerField('Năm sinh', null=True, blank=True, default=None)
    gender = models.CharField('Giới tính', max_length=10, choices=[('Nữ', 'Nữ'), ('Nam', 'Nam')], blank=True, default='')
    hometown = models.CharField('Quê quán', max_length=150, blank=True, default='')
    voice = models.CharField('Giọng nói', max_length=50, blank=True, default='')
    academic_level = models.CharField('Học vấn', max_length=100, blank=True, default='')
    graduation_detail = models.CharField(
        'Chi tiết tốt nghiệp & Chuyên ngành',
        max_length=255,
        blank=True,
        default=''
    )
    workplace = models.CharField(
        'Nơi công tác / Học tập hiện tại',
        max_length=255,
        blank=True,
        default=''
    )
    achievements = models.TextField(
        'Thành tích trong học tập và dạy học',
        blank=True,
        default=''
    )
    teaching_topics = models.TextField(
        'Chủ đề dạy (phân cách bằng dấu phẩy)',
        blank=True,
        default=''
    )
    tutor_type = models.CharField(
        'Gia sư đang là',
        max_length=50,
        choices=[
            ('Người đi làm', 'Người đi làm'),
            ('Sinh viên', 'Sinh viên'),
            ('Giáo viên', 'Giáo viên'),
            ('Cử nhân', 'Cử nhân'),
            ('Giảng viên', 'Giảng viên')
        ],
        blank=True,
        default=''
    )
    detailed_address = models.CharField(
        'Địa chỉ chi tiết',
        max_length=255,
        blank=True,
        default=''
    )
    birth_date = models.CharField('Ngày sinh', max_length=50, blank=True, default='')
    facebook_link = models.CharField('Kết nối Facebook của bạn', max_length=255, blank=True, default='')
    university = models.CharField('Trường đang học / đã tốt nghiệp', max_length=255, blank=True, default='')
    student_year = models.CharField('Sinh viên năm', max_length=50, blank=True, default='')
    major = models.CharField('Chuyên ngành', max_length=150, blank=True, default='')
    taught_classes_count = models.IntegerField('Số lượng lớp đã dạy', null=True, blank=True, default=None)
    
    # Ảnh xác nhận thông tin gia sư (CCCD & Thẻ SV/Bằng cấp)
    id_card_front = models.ImageField('Ảnh CMT/Căn cước/Hộ chiếu (Mặt trước)', upload_to='identity/', null=True, blank=True)
    student_card_1 = models.ImageField('Thẻ sinh viên/bằng/chứng chỉ 1', upload_to='certificates/', null=True, blank=True)
    student_card_2 = models.ImageField('Thẻ sinh viên/bằng/chứng chỉ 2', upload_to='certificates/', null=True, blank=True)
    student_card_3 = models.ImageField('Thẻ sinh viên/bằng/chứng chỉ 3', upload_to='certificates/', null=True, blank=True)

    available_schedule = models.TextField(
        'Lịch dạy tuần (JSON)',
        blank=True,
        default='{}'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hồ sơ Gia sư'
        verbose_name_plural = 'Danh sách Hồ sơ Gia sư'

    def __str__(self):
        name = self.user.profile.full_name if hasattr(self.user, 'profile') and self.user.profile.full_name else self.user.username
        return f"Gia sư: {name} - {self.get_approval_status_display()}"

    def get_topics_list(self):
        if self.teaching_topics and self.teaching_topics.strip():
            return [t.strip() for t in self.teaching_topics.split(',') if t.strip()]
        return []

    def get_achievements_list(self):
        if self.achievements and self.achievements.strip():
            lines = [line.strip().lstrip('-').lstrip('•').strip() for line in self.achievements.splitlines() if line.strip()]
            return lines
        return []

    def get_schedule_dict(self):
        import json
        if self.available_schedule:
            try:
                res = json.loads(self.available_schedule)
                if isinstance(res, dict):
                    return res
            except Exception:
                pass
        return {}

    @property
    def has_active_schedule(self):
        s = self.get_schedule_dict()
        return any(len(slots) > 0 for slots in s.values())

    @property
    def full_name(self):
        if hasattr(self.user, 'profile') and self.user.profile.full_name:
            return self.user.profile.full_name
        return self.user.get_full_name() or self.user.username

    @property
    def is_profile_completed(self):
        """
        Kiểm tra gia sư đã điền đầy đủ các thông tin cốt lõi của hồ sơ chưa:
        - Có chọn ít nhất 1 môn học sẽ dạy (subjects.exists())
        - Có thông tin học vấn / trường học (university hoặc education hoặc graduation_detail)
        - Có địa điểm nhận dạy hoặc địa chỉ chi tiết (location hoặc detailed_address)
        - Có họ tên đầy đủ
        """
        if not self.pk:
            return False
        has_subjects = self.subjects.exists()
        has_edu = bool(
            (self.university and self.university.strip()) or
            (self.education and self.education.strip()) or
            (self.graduation_detail and self.graduation_detail.strip())
        )
        has_location = bool(
            (self.location and self.location.strip()) or
            (self.detailed_address and self.detailed_address.strip())
        )
        has_name = bool(hasattr(self.user, 'profile') and self.user.profile.full_name and self.user.profile.full_name.strip())
        return bool(has_subjects and has_edu and has_location and has_name)

    def get_timetable_rows(self):
        """Trả về ma trận 3 hàng (Sáng, Chiều, Tối), mỗi hàng 7 ngày"""
        schedule = self.get_schedule_dict()
        days = [
            ('mon', 'Thứ 2'),
            ('tue', 'Thứ 3'),
            ('wed', 'Thứ 4'),
            ('thu', 'Thứ 5'),
            ('fri', 'Thứ 6'),
            ('sat', 'Thứ 7'),
            ('sun', 'Chủ nhật'),
        ]
        periods = [
            ('sang', 'Sáng'),
            ('chieu', 'Chiều'),
            ('toi', 'Tối'),
        ]
        matrix = []
        for p_key, p_name in periods:
            row_slots = []
            for d_key, d_name in days:
                is_active = (d_key in schedule and p_key in schedule[d_key])
                row_slots.append({
                    'day_key': d_key,
                    'day_name': d_name,
                    'period_key': p_key,
                    'period_name': p_name,
                    'is_active': is_active
                })
            matrix.append({
                'period_key': p_key,
                'period_name': p_name,
                'slots': row_slots
            })
        return matrix

    def get_split_timetable(self):
        """Trả về lịch chia làm 2 phần: Thứ 2 - Thứ 6 và Thứ 7 - Chủ nhật"""
        schedule = self.get_schedule_dict()
        weekdays = [('mon', 'Thứ 2'), ('tue', 'Thứ 3'), ('wed', 'Thứ 4'), ('thu', 'Thứ 5'), ('fri', 'Thứ 6')]
        weekend = [('sat', 'Thứ 7'), ('sun', 'Chủ nhật')]
        periods = [('sang', 'Sáng'), ('chieu', 'Chiều'), ('toi', 'Tối')]
        
        weekday_rows = []
        for p_key, p_name in periods:
            slots = []
            for d_key, d_name in weekdays:
                slots.append({
                    'day_key': d_key,
                    'day_name': d_name,
                    'period_key': p_key,
                    'period_name': p_name,
                    'is_active': (d_key in schedule and p_key in schedule[d_key])
                })
            weekday_rows.append({
                'period_name': p_name,
                'slots': slots
            })
            
        weekend_rows = []
        for p_key, p_name in periods:
            slots = []
            for d_key, d_name in weekend:
                slots.append({
                    'day_key': d_key,
                    'day_name': d_name,
                    'period_key': p_key,
                    'period_name': p_name,
                    'is_active': (d_key in schedule and p_key in schedule[d_key])
                })
            weekend_rows.append({
                'period_name': p_name,
                'slots': slots
            })
            
        return {
            'weekdays': weekdays,
            'weekday_rows': weekday_rows,
            'weekend': weekend,
            'weekend_rows': weekend_rows,
        }

    @property
    def full_name(self):
        if hasattr(self.user, 'profile') and self.user.profile.full_name:
            return self.user.profile.full_name
        return self.user.username

    @property
    def phone(self):
        return self.user.profile.phone if hasattr(self.user, 'profile') else ''

    @property
    def avatar_url(self):
        return self.user.profile.get_avatar_url() if hasattr(self.user, 'profile') else ''

    @property
    def is_certificate_image(self):
        if self.certificate_file:
            name = str(self.certificate_file.name).lower()
            return any(name.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif'])
        return False

    @property
    def is_certificate_pdf(self):
        if self.certificate_file:
            return str(self.certificate_file.name).lower().endswith('.pdf')
        return False

    def get_average_rating(self):
        avg = self.user.tutor_reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 5.0

    def get_review_count(self):
        return self.user.tutor_reviews.count()

    def get_completed_classes_count(self):
        return self.user.tutor_matched_classes.filter(status='completed').count()


class TutorCertificate(models.Model):
    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE, related_name='certificates')
    file = models.FileField('Tệp minh chứng', upload_to='certificates/')
    title = models.CharField('Tên tệp', max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Minh chứng Bằng cấp'
        verbose_name_plural = 'Danh sách Minh chứng Bằng cấp'
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or self.file.name

    @property
    def is_image(self):
        name = str(self.file.name).lower()
        return any(name.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif'])

    @property
    def is_pdf(self):
        return str(self.file.name).lower().endswith('.pdf')

    @property
    def filename(self):
        import os
        return os.path.basename(self.file.name)

