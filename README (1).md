# TutorLink – Website Kết Nối Học Sinh Và Gia Sư

TutorLink là dự án web của nhóm 5 thành viên, được xây dựng nhằm kết nối **Học sinh**, **Gia sư** và **Quản trị viên** trên cùng một hệ thống.

Hệ thống hỗ trợ **hai chiều kết nối**:

1. Học sinh chủ động tìm gia sư và gửi yêu cầu học.
2. Học sinh đăng bài cần gia sư, sau đó gia sư chủ động tìm lớp và ứng tuyển.

---

## 1. Mục tiêu dự án

Hiện nay việc tìm gia sư thường diễn ra qua Facebook, nhóm chat, người quen hoặc trung tâm. Các hạn chế thường gặp:

- Thông tin gia sư và lớp học bị phân tán.
- Khó so sánh học phí, kinh nghiệm và khu vực.
- Khó kiểm chứng hồ sơ gia sư.
- Học sinh mất nhiều thời gian tìm người phù hợp.
- Gia sư khó tìm lớp phù hợp với chuyên môn và lịch rảnh.
- Việc theo dõi trạng thái ứng tuyển, ghép lớp và đánh giá chưa tập trung.

TutorLink hướng tới một hệ thống đơn giản, dễ dùng và phù hợp với đồ án lập trình web.

---

## 2. Đối tượng sử dụng

### 2.1. Học sinh

Học sinh có thể:

- Đăng ký, đăng nhập, đăng xuất.
- Quản lý hồ sơ cá nhân.
- Tìm kiếm và lọc gia sư theo môn học, khu vực, học phí, hình thức Online/Offline.
- Xem chi tiết hồ sơ gia sư.
- Gửi yêu cầu học trực tiếp.
- Đăng bài cần tìm gia sư.
- Sửa, xóa, đóng bài đăng.
- Xem danh sách gia sư ứng tuyển.
- Đồng ý hoặc từ chối ứng viên.
- Theo dõi lớp đang học và lịch sử lớp.
- Đánh giá gia sư sau khi hoàn thành.

### 2.2. Gia sư

Gia sư có thể:

- Đăng ký, đăng nhập, đăng xuất.
- Tạo và cập nhật hồ sơ gia sư.
- Cập nhật môn dạy, kinh nghiệm, trình độ, học phí, khu vực, hình thức dạy.
- Xem danh sách lớp đang cần gia sư.
- Tìm kiếm và lọc lớp.
- Xem chi tiết lớp.
- Ứng tuyển nhận lớp.
- Nhận yêu cầu học trực tiếp từ học sinh.
- Đồng ý hoặc từ chối yêu cầu.
- Quản lý lớp đang dạy.
- Đánh dấu hoàn thành lớp.
- Xem đánh giá của học sinh.

### 2.3. Quản trị viên

Quản trị viên có thể:

- Đăng nhập trang quản trị.
- Xem Dashboard tổng quan.
- Quản lý tài khoản người dùng.
- Khóa/mở khóa tài khoản.
- Duyệt hoặc từ chối hồ sơ gia sư.
- Quản lý bài đăng tìm gia sư.
- Quản lý lượt ứng tuyển.
- Quản lý các lớp đã ghép.
- Quản lý đánh giá.
- Ẩn/xóa nội dung vi phạm.
- Xem thống kê hệ thống.

---

## 3. Luồng hoạt động chính

### 3.1. Học sinh chủ động tìm gia sư

```text
Học sinh
   ↓
Tìm kiếm / lọc gia sư
   ↓
Xem hồ sơ gia sư
   ↓
Gửi yêu cầu học
   ↓
Gia sư nhận yêu cầu
   ↓
Đồng ý / Từ chối
   ↓
Ghép lớp
   ↓
Đang học
   ↓
Hoàn thành
   ↓
Học sinh đánh giá
```

### 3.2. Gia sư chủ động tìm lớp

```text
Học sinh
   ↓
Đăng bài cần tìm gia sư
   ↓
Gia sư xem danh sách lớp
   ↓
Ứng tuyển nhận lớp
   ↓
Học sinh xem hồ sơ ứng viên
   ↓
Đồng ý / Từ chối
   ↓
Ghép lớp
   ↓
Đang học
   ↓
Hoàn thành
   ↓
Học sinh đánh giá
```

---

## 4. Trạng thái chính

| Trạng thái | Ý nghĩa |
|---|---|
| `pending` | Đang chờ xử lý |
| `accepted` | Đã được chấp nhận |
| `rejected` | Bị từ chối |
| `completed` | Đã hoàn thành |
| `cancelled` | Đã hủy |

Đối với hồ sơ gia sư:

| Trạng thái | Ý nghĩa |
|---|---|
| `pending` | Chờ Admin duyệt |
| `approved` | Đã được duyệt |
| `rejected` | Bị từ chối |

---

## 5. Công nghệ dự kiến

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript cơ bản

### Database

- SQLite khi phát triển.
- Có thể chuyển sang MySQL khi cần mở rộng.

### Quản lý mã nguồn

- Git
- GitHub

### Deploy dự kiến

- Render hoặc PythonAnywhere.

---

## 6. Cấu trúc dự án đề xuất

```text
TutorLink/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
├── tutors/
├── class_requests/
├── applications/
├── dashboard/
├── reviews/
│
├── templates/
│   ├── base.html
│   ├── accounts/
│   ├── student/
│   ├── tutor/
│   └── admin_dashboard/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/
```

---

## 7. Database dự kiến

### User

Thông tin đăng nhập mặc định của Django.

### UserProfile

Các trường gợi ý:

- user
- full_name
- phone
- address
- avatar
- role

Role:

- `student`
- `tutor`
- `admin`

### TutorProfile

- user
- introduction
- experience
- education
- price_per_hour
- location
- teaching_method
- approval_status

### Subject

Danh sách môn học, ví dụ:

- Toán
- Vật lý
- Hóa học
- Ngữ văn
- Tiếng Anh
- Tin học
- Python

### ClassRequest

Bài đăng tìm gia sư:

- student
- subject
- grade
- location
- budget
- schedule
- teaching_method
- description
- status
- created_at

### Application

Gia sư ứng tuyển:

- class_request
- tutor
- message
- status
- created_at

### StudyRequest

Học sinh gửi yêu cầu trực tiếp:

- student
- tutor
- subject
- schedule
- teaching_method
- note
- status
- created_at

### MatchedClass

Lớp đã ghép:

- student
- tutor
- subject
- start_date
- status

### Review

- student
- tutor
- matched_class
- rating
- comment
- created_at

---

## 8. Các trang chính

### Trang chung

```text
/
Trang chủ

/login/
Đăng nhập

/register/
Đăng ký

/profile/
Hồ sơ cá nhân
```

### Học sinh

```text
/student/dashboard/
/tutors/
/tutors/<id>/
/student/post-class/
/student/posts/
/student/requests/
/student/applications/
/student/classes/
```

### Gia sư

```text
/tutor/dashboard/
/tutor/profile/
/classes/
/classes/<id>/
/tutor/applications/
/tutor/requests/
/tutor/classes/
```

### Quản trị viên

```text
/admin-dashboard/
/admin-dashboard/users/
/admin-dashboard/tutors/
/admin-dashboard/posts/
/admin-dashboard/applications/
/admin-dashboard/classes/
/admin-dashboard/reviews/
/admin-dashboard/statistics/
```

---

## 9. Quy chuẩn giao diện

### Màu sắc chung

| Thành phần | Mã màu |
|---|---|
| Primary | `#2563EB` |
| Secondary | `#14B8A6` |
| Accent | `#F59E0B` |
| Background | `#F8FAFC` |
| Card | `#FFFFFF` |
| Text chính | `#0F172A` |
| Text phụ | `#64748B` |
| Border | `#E2E8F0` |
| Success | `#22C55E` |
| Warning | `#F59E0B` |
| Danger | `#EF4444` |

### Font

- Heading: Inter Bold
- Menu / Button: Inter Medium
- Nội dung: Inter Regular

### Component

- Button: bo góc 8px.
- Card: bo góc 12px.
- Input, button và card phải thống nhất giữa các thành viên.
- Ngày: `DD/MM/YYYY`.
- Giờ: định dạng 24 giờ.

---

## 10. Phân công nhóm 5 thành viên

### Thành viên 1 – Tài khoản và hệ thống chung

- Đăng ký.
- Đăng nhập.
- Đăng xuất.
- Phân quyền Student/Tutor/Admin.
- Hồ sơ cá nhân.
- Dashboard học sinh cơ bản.
- Navbar.
- Footer.
- `base.html`.
- Hỗ trợ ghép code tổng.

### Thành viên 2 – Học sinh và tìm gia sư

- Danh sách gia sư.
- Tìm kiếm/lọc gia sư.
- Trang chi tiết gia sư.
- Gửi yêu cầu học.
- Đăng bài tìm gia sư.
- Sửa/xóa/đóng bài đăng.

### Thành viên 3 – Gia sư và tìm lớp

- Hồ sơ gia sư.
- Dashboard gia sư.
- Quản lý môn dạy.
- Học phí.
- Kinh nghiệm.
- Danh sách lớp.
- Tìm kiếm/lọc lớp.
- Trang chi tiết lớp.

### Thành viên 4 – Ứng tuyển và ghép lớp

- Gia sư ứng tuyển.
- Học sinh xem ứng viên.
- Học sinh đồng ý/từ chối.
- Gia sư nhận yêu cầu học.
- Gia sư đồng ý/từ chối.
- Logic ghép lớp.
- Quản lý trạng thái lớp.
- Hoàn thành/hủy lớp.

### Thành viên 5 – Admin và đánh giá

- Dashboard Admin.
- Quản lý tài khoản.
- Khóa/mở tài khoản.
- Duyệt gia sư.
- Quản lý bài đăng.
- Quản lý lớp.
- Đánh giá gia sư.
- Quản lý đánh giá.
- Thống kê.

---

## 11. Quy tắc làm việc nhóm

### Branch đề xuất

```text
main
dev

feature/accounts
feature/tutors
feature/class-requests
feature/applications
feature/admin-dashboard
```

### Quy trình

```text
Tạo branch riêng
      ↓
Code chức năng
      ↓
Test chức năng
      ↓
Commit
      ↓
Push GitHub
      ↓
Pull Request
      ↓
Review
      ↓
Merge vào dev
      ↓
Test tổng
      ↓
Merge vào main
```

Không nên để 5 thành viên cùng code trực tiếp trên `main`.

---

## 12. Quy tắc commit

Ví dụ:

```bash
git commit -m "feat: add tutor search"
```

Tiền tố đề xuất:

```text
feat:      thêm chức năng mới
fix:       sửa lỗi
style:     chỉnh giao diện
refactor:  chỉnh lại code
docs:      cập nhật tài liệu
test:      thêm hoặc sửa kiểm thử
```

---

## 13. Cài đặt dự án

Clone repository:

```bash
git clone <repository-url>
cd TutorLink
```

Tạo môi trường ảo:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Cài thư viện:

```bash
pip install -r requirements.txt
```

Migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

Tạo tài khoản Admin:

```bash
python manage.py createsuperuser
```

Chạy server:

```bash
python manage.py runserver
```

Mở:

```text
http://127.0.0.1:8000/
```

---

## 14. Checklist trước Demo

### Học sinh

- [ ] Đăng ký.
- [ ] Đăng nhập.
- [ ] Tìm gia sư.
- [ ] Xem hồ sơ.
- [ ] Gửi yêu cầu học.
- [ ] Đăng bài tìm gia sư.
- [ ] Nhận ứng tuyển.
- [ ] Chọn gia sư.
- [ ] Ghép lớp.

### Gia sư

- [ ] Đăng ký.
- [ ] Tạo hồ sơ.
- [ ] Được Admin duyệt.
- [ ] Tìm lớp.
- [ ] Ứng tuyển.
- [ ] Nhận yêu cầu học.
- [ ] Đồng ý/từ chối.
- [ ] Quản lý lớp đang dạy.

### Admin

- [ ] Đăng nhập.
- [ ] Duyệt gia sư.
- [ ] Quản lý người dùng.
- [ ] Quản lý bài đăng.
- [ ] Quản lý đánh giá.

### Kết thúc lớp

- [ ] Ghép lớp.
- [ ] Đang học.
- [ ] Hoàn thành.
- [ ] Học sinh đánh giá gia sư.

---

## 15. Tài liệu cuối kỳ

### Technical Plan

- Tech Stack.
- Kiến trúc hệ thống.
- Database.
- Django Apps.
- Phân quyền.
- Cách chạy project.
- Cách deploy.

### Product Requirements Document – PRD

- Vấn đề.
- Đối tượng người dùng.
- Yêu cầu chức năng.
- User Flow.
- Must-have.
- Nice-to-have.

### Business Plan

- Khách hàng mục tiêu.
- Giá trị sản phẩm.
- Đối thủ.
- Mô hình phát triển.
- Hướng thương mại hóa.

### UX/UI & User Story

- Wireframe.
- Giao diện.
- User Story Học sinh.
- User Story Gia sư.
- User Story Admin.

### Project Demo

```text
Đăng nhập
→ Tìm / đăng lớp
→ Yêu cầu / ứng tuyển
→ Ghép lớp
→ Hoàn thành
→ Đánh giá
→ Admin quản lý
```

### Pitch Deck

1. Trang bìa.
2. Vấn đề thực tế.
3. Giải pháp TutorLink.
4. Ba đối tượng sử dụng.
5. Tính năng cốt lõi.
6. Luồng người dùng.
7. Công nghệ và kiến trúc.
8. Demo, hướng phát triển và Q&A.

---

## 16. Chức năng ưu tiên

### Must-have

- Đăng ký/đăng nhập.
- Phân quyền.
- Hồ sơ học sinh.
- Hồ sơ gia sư.
- Danh sách gia sư.
- Tìm kiếm/lọc gia sư.
- Đăng bài tìm gia sư.
- Danh sách lớp.
- Ứng tuyển.
- Gửi yêu cầu học.
- Chấp nhận/từ chối.
- Ghép lớp.
- Admin duyệt gia sư.
- Đánh giá.

### Nice-to-have

Chỉ làm sau khi chức năng cốt lõi ổn định:

- Chat.
- Email thông báo.
- Google Maps.
- AI gợi ý gia sư.
- Thanh toán trực tuyến.
- Lịch học nâng cao.
- Wishlist gia sư.
- Gia sư nổi bật.
- Push Notification.

---

## 17. Roadmap đề xuất

### Giai đoạn 1 – Chuẩn bị

- Chốt yêu cầu.
- Chốt database.
- Chốt giao diện.
- Tạo GitHub repository.
- Tạo Django project.

### Giai đoạn 2 – Chức năng nền tảng

- Authentication.
- Phân quyền.
- Hồ sơ.
- Database chính.

### Giai đoạn 3 – Học sinh và Gia sư

- Tìm gia sư.
- Đăng lớp.
- Tìm lớp.
- Ứng tuyển.
- Yêu cầu học.

### Giai đoạn 4 – Ghép lớp và Admin

- Logic trạng thái.
- Dashboard.
- Duyệt gia sư.
- Review.

### Giai đoạn 5 – Hoàn thiện

- Ghép code.
- Test.
- Sửa lỗi.
- Responsive.
- Deploy.
- Quay demo.
- Làm slide.

---

## 18. Thành viên nhóm

| STT | Thành viên | Phần phụ trách |
|---|---|---|
| 1 | Thành viên 1 | Tài khoản & hệ thống chung |
| 2 | Thành viên 2 | Học sinh & tìm gia sư |
| 3 | Thành viên 3 | Gia sư & tìm lớp |
| 4 | Thành viên 4 | Ứng tuyển & ghép lớp |
| 5 | Thành viên 5 | Admin & đánh giá |

> Cập nhật tên thật của từng thành viên sau khi nhóm chốt phân công.

---

## 19. Trạng thái dự án

**Đang lên kế hoạch và phát triển.**

- [ ] Chốt database
- [ ] Chốt giao diện
- [ ] Tạo Django project
- [ ] Authentication
- [ ] Hồ sơ gia sư
- [ ] Tìm gia sư
- [ ] Đăng lớp
- [ ] Tìm lớp
- [ ] Ứng tuyển
- [ ] Ghép lớp
- [ ] Admin
- [ ] Đánh giá
- [ ] Test
- [ ] Deploy
- [ ] Demo
- [ ] Pitch Deck

---

## 20. Nguyên tắc ưu tiên

Mục tiêu của nhóm là xây dựng một sản phẩm **đơn giản, chạy ổn định, luồng rõ ràng và dễ demo**.

Không nên triển khai AI, chat realtime, thanh toán hoặc các tính năng nâng cao trước khi phần cốt lõi hoàn thành ổn định.

---

# TutorLink

**Connecting students with the right tutors.**
