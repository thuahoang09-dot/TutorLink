from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os
from tutors.models import TutorProfile, Subject
from class_requests.models import ClassRequest
from matched_classes.models import MatchedClass
from accounts.models import UserProfile

def view_project_pdf(request):
    pdf_path = settings.BASE_DIR / 'TutorLink_Bao_Cao_Du_An.pdf'
    if not os.path.exists(pdf_path):
        pdf_path = settings.BASE_DIR / 'README.pdf'
    if not os.path.exists(pdf_path):
        raise Http404("PDF not found")
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

def home_view(request):
    featured_tutors = TutorProfile.objects.filter(
        approval_status='approved'
    ).select_related('user', 'user__profile').prefetch_related('subjects')[:6]

    latest_class_requests = ClassRequest.objects.filter(
        status='pending'
    ).select_related('student', 'student__profile', 'subject')[:6]

    total_tutors = TutorProfile.objects.filter(approval_status='approved').count()
    total_classes = MatchedClass.objects.count()
    total_students = UserProfile.objects.filter(role='student').count()
    subjects = Subject.objects.all().order_by('category', 'order', 'id')

    return render(request, 'home.html', {
        'featured_tutors': featured_tutors,
        'latest_class_requests': latest_class_requests,
        'total_tutors': total_tutors,
        'total_classes': total_classes,
        'total_students': total_students,
        'subjects': subjects,
    })


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def assistant_chat_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        data = request.POST

    query = data.get('message', '').strip()
    if not query:
        return JsonResponse({'reply': 'Xin chào! Bạn cần mình hỗ trợ thông tin gì về TutorLink ạ?'})

    q = query.lower()

    # Live context from database
    open_classes_count = ClassRequest.objects.filter(status='pending').count()
    approved_tutors_count = TutorProfile.objects.filter(approval_status='approved').count()

    # 1. TÌM LỚP / TÌM LỚP GIA SƯ / NHẬN LỚP DẠY (Dành cho gia sư)
    if any(k in q for k in ['tìm lớp', 'lớp gia sư', 'nhận lớp', 'ứng tuyển', 'lớp dạy', 'dạy kèm ở đâu', 'muốn đi dạy', 'có lớp nào', 'lớp cần gia sư']):
        reply = (
            f"Để <strong>tìm lớp nhận dạy</strong>, bạn hãy vào mục <strong>Lớp Cần Gia Sư</strong>.<br><br>"
            f"Hiện tại trên hệ thống đang có <strong>{open_classes_count} lớp học mới</strong> từ các phụ huynh đang chờ gia sư ứng tuyển với đầy đủ mức lương và địa chỉ/Online.<br><br>"
            f"<a href='/classes/' class='btn btn-sm btn-primary text-white fw-bold px-3 py-1.5' style='border-radius: 8px; text-decoration: none;'>"
            f"👉 Xem Danh Sách Lớp Cần Gia Sư</a>"
        )
        return JsonResponse({'reply': reply, 'intent': 'find_classes'})

    # 2. ĐĂNG BÀI / ĐĂNG TIN TÌM GIA SƯ
    if any(k in q for k in ['đăng bài', 'đăng tin', 'tạo lớp', 'cần tìm người dạy', 'đăng yêu cầu', 'đăng lớp']):
        reply = (
            f"Để đăng yêu cầu tìm gia sư, phụ huynh/học sinh chỉ cần vào trang <strong>Đăng Tìm Gia Sư</strong>:<br>"
            f"1. Điền môn học, khối lớp và học lực của học sinh.<br>"
            f"2. Chọn hình thức (Online hoặc Trực tiếp tại nhà) và lịch học.<br>"
            f"3. Đặt mức thù lao/buổi mong muốn.<br><br>"
            f"Sau khi đăng, các gia sư phù hợp sẽ trực tiếp nộp đơn ứng tuyển để bạn lựa chọn!<br><br>"
            f"<a href='/classes/post/' class='btn btn-sm btn-success text-white fw-bold px-3 py-1.5' style='border-radius: 8px; text-decoration: none;'>"
            f"📝 Đăng Tin Tìm Gia Sư Ngay</a>"
        )
        return JsonResponse({'reply': reply, 'intent': 'post_class'})

    # 3. TÌM GIA SƯ / CẦN GIA SƯ (Dành cho học sinh/phụ huynh)
    if any(k in q for k in ['tìm gia sư', 'cần gia sư', 'thuê gia sư', 'học kèm', 'tìm thầy', 'tìm cô', 'kiếm gia sư']):
        reply = (
            f"TutorLink hiện có hơn <strong>{approved_tutors_count} gia sư giỏi</strong> (sinh viên xuất sắc từ các trường ĐH top đầu và giáo viên uy tín) đã được kiểm duyệt hồ sơ.<br><br>"
            f"Bạn có thể lọc hồ sơ theo môn học, khu vực tỉnh/thành, quận/huyện và mức học phí mong muốn tại đây:<br><br>"
            f"<a href='/tutors/' class='btn btn-sm btn-primary text-white fw-bold px-3 py-1.5' style='border-radius: 8px; text-decoration: none;'>"
            f"👉 Xem Danh Sách Gia Sư Giỏi</a>"
        )
        return JsonResponse({'reply': reply, 'intent': 'find_tutors'})

    # 4. HỌC PHÍ / BẢNG GIÁ
    if any(k in q for k in ['học phí', 'giá', 'chi phí', 'bao nhiêu tiền', 'bảng giá', 'mức lương', 'tiền học']):
        reply = (
            f"Mức học phí trên TutorLink rất minh bạch và linh hoạt:<br>"
            f"• <strong>Gia sư Sinh viên giỏi:</strong> 120.000đ – 180.000đ/giờ (khoảng 150k - 200k/buổi)<br>"
            f"• <strong>Giáo viên / Thạc sĩ:</strong> 200.000đ – 350.000đ/giờ<br>"
            f"• <strong>Luyện thi IELTS / Chứng chỉ / Chuyên sâu:</strong> 350.000đ – 500.000đ+/giờ<br><br>"
            f"Bạn có thể lọc trực tiếp theo mức học phí ở thanh tìm kiếm của trang <strong>Tìm Gia Sư</strong>!"
        )
        return JsonResponse({'reply': reply, 'intent': 'pricing'})

    # 5. ĐĂNG KÝ GIA SƯ / LÀM GIA SƯ
    if any(k in q for k in ['đăng ký gia sư', 'làm gia sư', 'trở thành gia sư', 'hồ sơ gia sư', 'đăng ký dạy']):
        reply = (
            f"Để trở thành gia sư trên TutorLink, bạn thực hiện các bước sau:<br>"
            f"1. Nhấn <a href='/accounts/register/?role=tutor' class='fw-bold text-primary'>Đăng Ký Tài Khoản</a> và chọn vai trò <strong>Gia sư</strong>.<br>"
            f"2. Vào mục Hồ sơ cập nhật thông tin học vấn, bằng cấp và môn thế mạnh.<br>"
            f"3. Ban Quản Trị sẽ kiểm duyệt hồ sơ trong vòng 24h. Sau khi được duyệt, bạn có thể nhận lớp ngay!"
        )
        return JsonResponse({'reply': reply, 'intent': 'register_tutor'})

    # 6. QUY TRÌNH GHÉP LỚP
    if any(k in q for k in ['quy trình', 'ghép lớp', 'cách thức', 'hoạt động', 'bảo đảm']):
        reply = (
            f"Quy trình ghép lớp 2 chiều thông minh tại TutorLink:<br>"
            f"1️⃣ <strong>Kết nối 2 chiều:</strong> Học sinh chủ động chọn gia sư HOẶC đăng bài để gia sư tự ứng tuyển.<br>"
            f"2️⃣ <strong>Phê duyệt:</strong> Học sinh xem hồ sơ ứng viên và bấm <em>Chấp nhận</em>.<br>"
            f"3️⃣ <strong>Kích hoạt lớp:</strong> Hệ thống tự động ghép lớp và mở thông tin liên lạc trực tiếp giữa 2 bên.<br>"
            f"4️⃣ <strong>Đánh giá:</strong> Học sinh đánh giá chất lượng dạy sau khi hoàn thành khóa học."
        )
        return JsonResponse({'reply': reply, 'intent': 'process'})

    # 7. LIÊN HỆ / HOTLINE / HỖ TRỢ
    if any(k in q for k in ['hotline', 'liên hệ', 'số điện thoại', 'sđt', 'admin', 'quản trị viên', 'hỗ trợ', 'tư vấn', 'khiếu nại']):
        reply = (
            f"Ban Quản Trị TutorLink luôn sẵn sàng hỗ trợ bạn:<br>"
            f"📞 <strong>Hotline:</strong> 1900 6868 (8h00 - 21h00 hàng ngày)<br>"
            f"✉️ <strong>Email:</strong> contact@tutorlink.edu.vn<br>"
            f"🏢 <strong>Văn phòng:</strong> Khoa CNTT - ĐH Quốc Gia<br>"
            f"🌐 <strong>Hỗ trợ trực tuyến:</strong> 24/7."
        )
        return JsonResponse({'reply': reply, 'intent': 'contact'})

    # 8. MÔN HỌC CỤ THỂ (Toán, Lý, Hóa, Văn, Tiếng Anh, IELTS, Lập trình...)
    subjects = Subject.objects.all()
    for sub in subjects:
        if sub.name.lower() in q:
            reply = (
                f"Bạn đang quan tâm đến môn <strong>{sub.name}</strong> đúng không?<br><br>"
                f"TutorLink có đội ngũ gia sư chuyên dạy kèm <strong>{sub.name}</strong> từ căn bản đến nâng cao và luyện thi cấp tốc.<br><br>"
                f"<a href='/tutors/?subject={sub.id}' class='btn btn-sm btn-primary text-white fw-bold px-3 py-1.5' style='border-radius: 8px; text-decoration: none;'>"
                f"👉 Xem Gia Sư Môn {sub.name}</a>"
            )
            return JsonResponse({'reply': reply, 'intent': 'subject_specific'})

    # 9. CHÀO HỎI
    if any(k in q for k in ['chào', 'hello', 'hi', 'bạn là ai', 'alo', 'ê']):
        user_name = "bạn"
        if request.user.is_authenticated:
            user_name = getattr(getattr(request.user, 'profile', None), 'full_name', None) or request.user.username
        reply = (
            f"Xin chào <strong>{user_name}</strong>! Mình là <strong>TutorLink AI Assistant</strong> 🎓.<br>"
            f"Mình được tích hợp để giải đáp tức thì về tìm gia sư, tìm lớp dạy, đăng tin, mức học phí và quy trình học.<br><br>"
            f"Bạn có thể gõ câu hỏi hoặc chọn các nút gợi ý bên trên nhé!"
        )
        return JsonResponse({'reply': reply, 'intent': 'greeting'})

    # Default Contextual Response
    reply = (
        f"Mình đã nhận được câu hỏi: <em>\"{query}\"</em>.<br><br>"
        f"Bạn có thể tham khảo nhanh các dịch vụ của TutorLink:<br>"
        f"• <a href='/tutors/' class='fw-bold text-primary'>Tìm gia sư giỏi</a> theo môn & khu vực.<br>"
        f"• <a href='/classes/' class='fw-bold text-primary'>Xem lớp cần gia sư</a> để nhận lớp dạy.<br>"
        f"• <a href='/classes/post/' class='fw-bold text-success'>Đăng bài cần gia sư</a> miễn phí.<br><br>"
        f"Hoặc liên hệ tổng đài <strong>1900 6868</strong> để được hỗ trợ trực tiếp 24/7 nhé!"
    )
    return JsonResponse({'reply': reply, 'intent': 'general'})

