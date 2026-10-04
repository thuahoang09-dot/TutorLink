import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile
from tutors.models import Subject, TutorProfile
from class_requests.models import ClassRequest
from applications.models import Application
from study_requests.models import StudyRequest
from matched_classes.models import MatchedClass
from reviews.models import Review

class Command(BaseCommand):
    help = 'Populates the database with realistic sample data for TutorLink demo'

    def handle(self, *args, **options):
        self.stdout.write('Khoi tao du lieu mau cho TutorLink...')

        # 1. Tao Subjects (22 mon hoc theo 3 nhom)
        subjects_data = [
            # Nhom 1: Mon pho thong
            {'name': 'Toán', 'slug': 'toan', 'category': 'pho_thong', 'order': 1, 'icon': 'bi-calculator', 'description': 'Toán từ tiểu học, THCS đến THPT, luyện thi vào 10 và thi tốt nghiệp.'},
            {'name': 'Lý', 'slug': 'ly', 'category': 'pho_thong', 'order': 2, 'icon': 'bi-lightning-charge', 'description': 'Vật lý THCS, THPT, bồi dưỡng học sinh giỏi và luyện thi đại học.'},
            {'name': 'Hóa', 'slug': 'hoa', 'category': 'pho_thong', 'order': 3, 'icon': 'bi-radioactive', 'description': 'Hóa học cơ bản và nâng cao, vô cơ, hữu cơ và giải đề.'},
            {'name': 'Văn', 'slug': 'van', 'category': 'pho_thong', 'order': 4, 'icon': 'bi-book-half', 'description': 'Ngữ văn, cảm thụ văn học, phân tích tác phẩm và luyện viết.'},
            {'name': 'Tiếng Việt', 'slug': 'tieng-viet', 'category': 'pho_thong', 'order': 5, 'icon': 'bi-pen', 'description': 'Tiếng Việt bậc tiểu học, rèn đọc, viết chính tả và ngữ pháp.'},
            {'name': 'Toán + Tiếng Việt', 'slug': 'toan-tieng-viet', 'category': 'pho_thong', 'order': 6, 'icon': 'bi-journals', 'description': 'Gia sư kết hợp Toán và Tiếng Việt cho học sinh tiểu học (Lớp 1 - 5).'},
            {'name': 'Lịch sử', 'slug': 'lich-su', 'category': 'pho_thong', 'order': 7, 'icon': 'bi-hourglass-split', 'description': 'Lịch sử Việt Nam và thế giới, sơ đồ tư duy ghi nhớ sự kiện.'},
            {'name': 'Địa lý', 'slug': 'dia-ly', 'category': 'pho_thong', 'order': 8, 'icon': 'bi-globe-americas', 'description': 'Địa lý tự nhiên, kinh tế - xã hội, kỹ năng đọc Atlat và phân tích số liệu.'},
            {'name': 'Sinh học', 'slug': 'sinh-hoc', 'category': 'pho_thong', 'order': 9, 'icon': 'bi-flower1', 'description': 'Sinh học cơ bản, di truyền học và ôn thi THPT Quốc gia.'},
            {'name': 'Luyện chữ', 'slug': 'luyen-chu', 'category': 'pho_thong', 'order': 10, 'icon': 'bi-brush', 'description': 'Rèn chữ đẹp, tư thế ngồi viết chuẩn cho học sinh tiền tiểu học và tiểu học.'},
            {'name': 'Tin học', 'slug': 'tin-hoc', 'category': 'pho_thong', 'order': 11, 'icon': 'bi-laptop', 'description': 'Tin học văn phòng, lập trình Scratch, Python, Pascal, luyện thi Tin học trẻ.'},
            {'name': 'Khoa học tự nhiên', 'slug': 'khoa-hoc-tu-nhien', 'category': 'pho_thong', 'order': 12, 'icon': 'bi-compass', 'description': 'Môn KHTN tích hợp Vật lý, Hóa học, Sinh học chương trình mới THCS.'},
            # Nhom 2: Mon ngoai ngu
            {'name': 'Tiếng Anh', 'slug': 'tieng-anh', 'category': 'ngoai_ngu', 'order': 1, 'icon': 'bi-translate', 'description': 'Tiếng Anh giao tiếp, ngữ pháp trường lớp, luyện thi IELTS, TOEIC, Cambridge.'},
            {'name': 'Tiếng Nhật', 'slug': 'tieng-nhat', 'category': 'ngoai_ngu', 'order': 2, 'icon': 'bi-chat-dots', 'description': 'Tiếng Nhật sơ cấp, trung cấp, luyện thi JLPT từ N5 đến N1.'},
            {'name': 'Tiếng Hàn', 'slug': 'tieng-han', 'category': 'ngoai_ngu', 'order': 3, 'icon': 'bi-chat-quote', 'description': 'Tiếng Hàn giao tiếp, luyện thi TOPIK I và II, chuẩn bị du học.'},
            {'name': 'Tiếng Trung', 'slug': 'tieng-trung', 'category': 'ngoai_ngu', 'order': 4, 'icon': 'bi-chat-left-text', 'description': 'Tiếng Trung giao tiếp, phát âm chuẩn Pinyin, luyện thi HSK 1 - 6.'},
            {'name': 'Tiếng Pháp', 'slug': 'tieng-phap', 'category': 'ngoai_ngu', 'order': 5, 'icon': 'bi-chat-square-text', 'description': 'Tiếng Pháp căn bản, luyện thi chứng chỉ DELF / DALF các cấp độ.'},
            {'name': 'Tiếng Đức', 'slug': 'tieng-duc', 'category': 'ngoai_ngu', 'order': 6, 'icon': 'bi-chat', 'description': 'Tiếng Đức A1 - B2, luyện thi chứng chỉ Goethe phục vụ du học nghề.'},
            # Nhom 3: The thao & Nghe thuat
            {'name': 'Âm nhạc - Đàn', 'slug': 'am-nhac-dan', 'category': 'the_thao_nghe_thuat', 'order': 1, 'icon': 'bi-music-note-beamed', 'description': 'Dạy kèm đàn Piano, Guitar, Organ, Ukulele, thanh nhạc cơ bản và nâng cao.'},
            {'name': 'Hội họa', 'slug': 'hoi-hoa', 'category': 'the_thao_nghe_thuat', 'order': 2, 'icon': 'bi-palette', 'description': 'Vẽ tranh màu nước, sáp dầu, vẽ chì, luyện thi khối V, khối H ngành kiến trúc, mỹ thuật.'},
            {'name': 'Dance ( Nhảy )', 'slug': 'dance-nhay', 'category': 'the_thao_nghe_thuat', 'order': 3, 'icon': 'bi-activity', 'description': 'Dạy nhảy hiện đại, Kpop cover, Hip-hop, Shuffle dance giúp rèn luyện thể chất và tự tin.'},
            {'name': 'Thể thao', 'slug': 'the-thao', 'category': 'the_thao_nghe_thuat', 'order': 4, 'icon': 'bi-trophy', 'description': 'Huấn luyện bơi lội, bóng đá, bóng rổ, cầu lông, cờ vua nâng cao sức khỏe.'},
        ]

        subject_objs = {}
        for s in subjects_data:
            obj, _ = Subject.objects.update_or_create(name=s['name'], defaults=s)
            subject_objs[s['slug']] = obj
        # Aliases for backwards compatibility with seed data
        subject_objs['toan-hoc'] = subject_objs['toan']
        subject_objs['vat-ly'] = subject_objs['ly']
        subject_objs['hoa-hoc'] = subject_objs['hoa']
        subject_objs['ngu-van'] = subject_objs['van']
        subject_objs['tin-hoc-python'] = subject_objs['tin-hoc']
        self.stdout.write(self.style.SUCCESS(f'[OK] Khoi tao {len(subjects_data)} mon hoc theo 3 nhom.'))


        # 2. Tao Admin
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@tutorlink.edu.vn',
                'first_name': 'Quản Trị Viên',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            admin_user.profile.role = 'admin'
            admin_user.profile.full_name = 'Ban Quản Trị TutorLink'
            admin_user.profile.phone = '19006868'
            admin_user.profile.save()
        self.stdout.write(self.style.SUCCESS('[OK] Tao Admin: admin / admin123'))

        # 3. Tao Students
        students_data = [
            {
                'username': 'hocsinh1',
                'email': 'nam.nguyen@example.com',
                'full_name': 'Nguyễn Hoàng Nam',
                'phone': '0912345678',
                'address': 'Quận Cầu Giấy, Hà Nội',
            },
            {
                'username': 'hocsinh2',
                'email': 'trang.tran@example.com',
                'full_name': 'Trần Thu Trang',
                'phone': '0987654321',
                'address': 'Quận 1, TP. Hồ Chí Minh',
            }
        ]

        student_objs = []
        for s_data in students_data:
            user, s_created = User.objects.get_or_create(
                username=s_data['username'],
                defaults={'email': s_data['email'], 'first_name': s_data['full_name']}
            )
            if s_created:
                user.set_password('123456')
                user.save()
            user.profile.role = 'student'
            user.profile.full_name = s_data['full_name']
            user.profile.phone = s_data['phone']
            user.profile.address = s_data['address']
            user.profile.save()
            student_objs.append(user)
        self.stdout.write(self.style.SUCCESS('[OK] Tao Hoc sinh: hocsinh1 / 123456, hocsinh2 / 123456'))

        # 4. Tao Tutors
        tutors_data = [
            {
                'username': 'giasu_toan',
                'email': 'tuan.toan@example.com',
                'full_name': 'Vũ Minh Tuấn',
                'phone': '0934567890',
                'address': 'Hà Nội',
                'subjects': ['toan-hoc', 'vat-ly'],
                'introduction': 'Chào phụ huynh và các em học sinh! Thầy Tuấn tốt nghiệp Thạc sĩ Đại học Sư Phạm Hà Nội, có hơn 5 năm kinh nghiệm chuyên luyện thi Đại học khối A và B. Phương pháp dạy tư duy bản chất, không học vẹt, biến các bài toán phức tạp thành các dạng quen thuộc dễ nhớ.',
                'education': 'Thạc sĩ Sư Phạm Toán - ĐH Sư Phạm Hà Nội (Tốt nghiệp loại Xuất sắc)',
                'experience': '5 năm giảng dạy tại trung tâm luyện thi danh tiếng và dạy kèm tại nhà. Đã giúp hơn 120 học sinh đạt điểm 8+ và 9+ môn Toán trong kỳ thi Tốt nghiệp THPT.',
                'price_per_hour': 200000,
                'location': 'Hà Nội (Nhận dạy các quận Cầu Giấy, Đống Đa, Nam Từ Liêm)',
                'teaching_method': 'both',
                'approval_status': 'approved',
            },
            {
                'username': 'giasu_anh',
                'email': 'maianh.eng@example.com',
                'full_name': 'Lê Mai Anh',
                'phone': '0967891234',
                'address': 'Hà Nội',
                'subjects': ['tieng-anh'],
                'introduction': 'Hello everyone! Cô Mai Anh có chứng chỉ IELTS 8.0 (Speaking 8.5) và chứng chỉ TESOL quốc tế. Với phong cách dạy năng động, gần gũi và thực tế, cô cam kết giúp học viên tự tin phản xạ tiếng Anh chỉ sau 3 tháng.',
                'education': 'Cử nhân Kinh tế đối ngoại - ĐH Ngoại Thương Hà Nội; IELTS 8.0 Overall; Chứng chỉ sư phạm quốc tế TESOL.',
                'experience': '4 năm chuyên luyện thi IELTS từ con số 0 lên 6.5+ và gia sư tiếng Anh THCS, THPT. Từng đạt học bổng trao đổi sinh viên tại Singapore.',
                'price_per_hour': 250000,
                'location': 'Hà Nội & Online Toàn Quốc',
                'teaching_method': 'both',
                'approval_status': 'approved',
            },
            {
                'username': 'giasu_tin',
                'email': 'huy.cntt@example.com',
                'full_name': 'Đặng Quốc Huy',
                'phone': '0901239876',
                'address': 'TP. Hồ Chí Minh',
                'subjects': ['tin-hoc-python'],
                'introduction': 'Kỹ sư phần mềm đam mê giáo dục công nghệ. Chuyên hướng dẫn lập trình căn bản đến nâng cao (Python, thuật toán, Web cơ bản) cho học sinh từ cấp 2 trở lên và người mới bắt đầu.',
                'education': 'Kỹ sư Công nghệ Thông tin - ĐH Bách Khoa TP.HCM (GPA 3.6/4.0)',
                'experience': '3 năm làm việc tại công ty công nghệ và dạy kèm lập trình cho học sinh tham gia kỳ thi Tin học trẻ.',
                'price_per_hour': 220000,
                'location': 'TP. Hồ Chí Minh & Online',
                'teaching_method': 'online',
                'approval_status': 'approved',
            },
            {
                'username': 'giasu_ly',
                'email': 'thang.vatly@example.com',
                'full_name': 'Phạm Đức Thắng',
                'phone': '0978112233',
                'address': 'Đà Nẵng',
                'subjects': ['vat-ly'],
                'introduction': 'Gia sư môn Vật lý nhiệt tình, phương pháp dạy trực quan bằng các thí nghiệm mô phỏng sinh động.',
                'education': 'Cử nhân Khoa học Vật lý - ĐH Khoa học Tự nhiên',
                'experience': '2 năm dạy kèm môn Vật lý cho học sinh lớp 10, 11, 12.',
                'price_per_hour': 180000,
                'location': 'Đà Nẵng',
                'teaching_method': 'offline',
                'approval_status': 'pending', # Cho Admin duyet de test chuc nang duyet!
            },
        ]

        tutor_objs = []
        for t_data in tutors_data:
            user, t_created = User.objects.get_or_create(
                username=t_data['username'],
                defaults={'email': t_data['email'], 'first_name': t_data['full_name']}
            )
            if t_created:
                user.set_password('123456')
                user.save()
            user.profile.role = 'tutor'
            user.profile.full_name = t_data['full_name']
            user.profile.phone = t_data['phone']
            user.profile.address = t_data['address']
            user.profile.save()

            tp, _ = TutorProfile.objects.get_or_create(user=user)
            tp.introduction = t_data['introduction']
            tp.education = t_data['education']
            tp.experience = t_data['experience']
            tp.price_per_hour = t_data['price_per_hour']
            tp.location = t_data['location']
            tp.teaching_method = t_data['teaching_method']
            tp.approval_status = t_data['approval_status']
            tp.save()

            for slug in t_data['subjects']:
                if slug in subject_objs:
                    tp.subjects.add(subject_objs[slug])

            tutor_objs.append(user)
        self.stdout.write(self.style.SUCCESS('[OK] Tao 4 Gia su: giasu_toan, giasu_anh, giasu_tin, giasu_ly / 123456'))

        # 5. Tao Bai dang tim gia su (ClassRequests)
        cr1, _ = ClassRequest.objects.get_or_create(
            title='Tìm gia sư Toán lớp 12 luyện thi Tốt nghiệp THPT & ĐGNL',
            student=student_objs[0],
            defaults={
                'subject': subject_objs['toan-hoc'],
                'grade': 'Lớp 12',
                'location': 'Quận Cầu Giấy, Hà Nội',
                'budget': 250000,
                'budget_type': 'per_session',
                'schedule': 'Thứ 3 - 5 - 7 từ 19h30 đến 21h30',
                'teaching_method': 'both',
                'description': 'Học sinh đang có học lực khá (khoảng 7.0 điểm môn Toán), mục tiêu thi khối A đạt 8.5+ điểm. Cần gia sư có phương pháp giải nhanh, bấm máy tính thành thạo và nắm chắc các dạng câu hỏi vận dụng cao.',
                'status': 'pending',
            }
        )

        cr2, _ = ClassRequest.objects.get_or_create(
            title='Cần gia sư Tiếng Anh cấp tốc lớp 11 chuẩn bị thi IELTS 6.5',
            student=student_objs[1],
            defaults={
                'subject': subject_objs['tieng-anh'],
                'grade': 'Lớp 11',
                'location': 'Quận 1, TP. Hồ Chí Minh hoặc Online',
                'budget': 250000,
                'budget_type': 'per_hour',
                'schedule': 'Tối thứ 2, 4, 6 từ 20h00',
                'teaching_method': 'online',
                'description': 'Em muốn củng cố phát âm, kỹ năng Viết và Nói. Hiện tại từ vựng còn hạn chế và ngữ pháp chưa vững. Mong muốn gia sư kiên nhẫn, sửa bài chi tiết hàng tuần.',
                'status': 'pending',
            }
        )

        cr3, _ = ClassRequest.objects.get_or_create(
            title='Tìm thầy dạy Lập trình Python cơ bản cho bé lớp 7',
            student=student_objs[0],
            defaults={
                'subject': subject_objs['tin-hoc-python'],
                'grade': 'Lớp 7',
                'location': 'Học Online qua Zoom/Meet',
                'budget': 200000,
                'budget_type': 'per_session',
                'schedule': 'Chiều thứ 7 và sáng Chủ Nhật',
                'teaching_method': 'online',
                'description': 'Bé rất thích máy tính và tò mò về lập trình game. Muốn tìm gia sư hướng dẫn nhập môn Python từ các khái niệm cơ bản, làm bài tập vui nhộn tạo cảm hứng.',
                'status': 'accepted',
            }
        )
        self.stdout.write(self.style.SUCCESS('[OK] Tao 3 bai dang tim gia su.'))

        # 6. Tao Don ung tuyen (Application)
        app1, _ = Application.objects.get_or_create(
            class_request=cr1,
            tutor=tutor_objs[0],
            defaults={
                'message': 'Chào em Nam! Thầy là Tuấn, chuyên luyện thi Toán 12. Thầy có sẵn giáo trình trọng tâm 40 dạng đề mới nhất của Bộ GD. Lịch tối 3-5-7 thầy hoàn toàn trống và có thể bắt đầu dạy thử ngay.',
                'proposed_price': 250000,
                'status': 'pending',
            }
        )

        app2, _ = Application.objects.get_or_create(
            class_request=cr3,
            tutor=tutor_objs[2],
            defaults={
                'message': 'Chào phụ huynh! Em là Huy, có kinh nghiệm dạy lập trình khối trung học. Em có giáo trình làm game Flappy Bird và giải đố bằng Python rất hợp với các bạn lớp 7.',
                'proposed_price': 200000,
                'status': 'accepted',
            }
        )
        self.stdout.write(self.style.SUCCESS('[OK] Tao 2 don ung tuyen nhan lop.'))

        # 7. Tao Lop da ghep (MatchedClass)
        mc1, _ = MatchedClass.objects.get_or_create(
            class_request=cr3,
            defaults={
                'student': student_objs[0],
                'tutor': tutor_objs[2],
                'subject': subject_objs['tin-hoc-python'],
                'schedule': 'Chiều thứ 7 và sáng Chủ Nhật',
                'hourly_rate': 200000,
                'teaching_method': 'online',
                'status': 'in_progress',
            }
        )

        mc2, _ = MatchedClass.objects.get_or_create(
            student=student_objs[1],
            tutor=tutor_objs[1],
            subject=subject_objs['tieng-anh'],
            defaults={
                'schedule': 'Tối 2-4-6 từ 19h00',
                'hourly_rate': 250000,
                'teaching_method': 'both',
                'status': 'completed',
            }
        )
        self.stdout.write(self.style.SUCCESS('[OK] Tao 2 lop hoc da ghep.'))

        # 8. Tao Danh gia (Review) cho lop da hoan thanh
        Review.objects.get_or_create(
            matched_class=mc2,
            defaults={
                'student': student_objs[1],
                'tutor': tutor_objs[1],
                'rating': 5,
                'comment': 'Cô Mai Anh dạy cực kỳ nhiệt tình và dễ hiểu! Sau 2 tháng học cùng cô, điểm Writing của em từ 5.0 đã lên được 6.5 và tự tin nói chuyện trôi chảy hơn rất nhiều. Cảm ơn cô và nền tảng TutorLink!'
            }
        )
        self.stdout.write(self.style.SUCCESS('[OK] Tao danh gia mau 5 sao.'))

        self.stdout.write(self.style.SUCCESS('\n=== HOAN TAT KHOI TAO DU LIEU MAU CHO TUTORLINK! ==='))
        self.stdout.write('Tai khoan co san:')
        self.stdout.write('1. Admin: admin / admin123')
        self.stdout.write('2. Hoc sinh: hocsinh1 / 123456 hoac hocsinh2 / 123456')
        self.stdout.write('3. Gia su (Approved): giasu_toan / 123456 hoac giasu_anh / 123456')
        self.stdout.write('4. Gia su (Pending): giasu_ly / 123456')

