/**
 * TutorLink Internationalization (i18n) Engine
 * Hỗ trợ chuyển đổi song ngữ Tiếng Việt (vi) và Tiếng Anh (en) toàn diện 100%.
 * Tích hợp tự động với UI Switcher, lưu trạng thái vào localStorage và dịch toàn diện DOM.
 */

(function(window, document) {
    'use strict';

    // 1. TỪ ĐIỂN KHÓA CẤU TRÚC (Structured Key-Value Dictionary)
    const TRANSLATIONS = {
        // --- Navigation & Brand ---
        brand_name: { vi: 'TutorLink', en: 'TutorLink' },
        nav_home: { vi: 'Trang chủ', en: 'Home' },
        nav_find_tutor: { vi: 'Dành cho Phụ huynh', en: 'For Parents' },
        nav_classes: { vi: 'Dành cho Gia sư', en: 'For Tutors' },
        nav_post_class: { vi: 'Đăng Tìm Gia Sư', en: 'Post Request' },
        nav_dashboard: { vi: 'Bảng điều khiển', en: 'Dashboard' },
        nav_my_posts: { vi: 'Bài đăng của tôi', en: 'My Posts' },
        nav_study_requests: { vi: 'Yêu cầu học', en: 'Study Requests' },
        nav_admin: { vi: 'Quản Trị Viên', en: 'Admin Portal' },
        nav_login: { vi: 'Đăng nhập', en: 'Log In' },
        nav_register: { vi: 'Đăng ký', en: 'Sign Up' },

        // --- Notifications (Facebook Style) ---
        notif_title: { vi: 'Thông báo', en: 'Notifications' },
        notif_mark_read: { vi: 'Đánh dấu đã đọc', en: 'Mark all as read' },
        notif_all: { vi: 'Tất cả', en: 'All' },
        notif_unread: { vi: 'Chưa đọc', en: 'Unread' },
        notif_empty_title: { vi: 'Không có thông báo mới', en: 'No new notifications' },
        notif_empty_sub: { vi: 'Thông báo nhận lớp hoặc nhận gia sư sẽ xuất hiện tại đây', en: 'Notifications for class matching or applications will appear here' },

        // --- User Menu & Settings ---
        profile: { vi: 'Thông tin cá nhân', en: 'My Profile' },
        edit_tutor_profile: { vi: 'Cập nhật hồ sơ gia sư', en: 'Edit Tutor Profile' },
        my_classes: { vi: 'Lớp học của tôi', en: 'My Classes' },
        my_applications: { vi: 'Lớp đã ứng tuyển', en: 'Applied Classes' },
        sent_requests: { vi: 'Yêu cầu học đã gửi', en: 'Sent Requests' },
        settings_title: { vi: 'Cài đặt hệ thống', en: 'System Settings' },
        theme_label: { vi: 'Giao diện', en: 'Theme' },
        theme_light: { vi: 'Sáng', en: 'Light' },
        theme_dark: { vi: 'Tối', en: 'Dark' },
        lang_label: { vi: 'Ngôn ngữ', en: 'Language' },
        lang_vi: { vi: 'Tiếng Việt', en: 'Vietnamese' },
        lang_en: { vi: 'Tiếng Anh', en: 'English' },
        logout: { vi: 'Đăng xuất', en: 'Log Out' },
        login: { vi: 'Đăng nhập', en: 'Log In' },
        register: { vi: 'Đăng ký', en: 'Sign Up' },
        role_student: { vi: 'HỌC SINH', en: 'STUDENT' },
        role_tutor: { vi: 'GIA SƯ', en: 'TUTOR' },
        role_admin: { vi: 'QUẢN TRỊ VIÊN', en: 'ADMIN' },

        // --- Homepage Hero & Promo Banner ---
        hero_special_deal: { vi: 'Ưu Đãi Đặc Biệt', en: 'Special Offer' },
        hero_banner1_title: { vi: 'Miễn Phí 100% Phí Kết Nối & Đăng Tin Tìm Gia Sư', en: '100% Free Connection Fee & Tutor Request Posting' },
        hero_banner1_sub: { vi: 'Hỗ trợ phụ huynh đổi gia sư miễn phí trong các buổi đầu nếu không phù hợp phương pháp học.', en: 'Free tutor exchange for parents during the first sessions if teaching methods do not match.' },
        hero_verified_badge: { vi: 'Hồ sơ xác thực 100%', en: '100% Verified Profiles' },
        hero_platform_tag: { vi: 'Nền tảng kết nối gia sư uy tín', en: 'Reputable Tutor Connection Platform' },
        hero_banner2_title_1: { vi: 'GIA SƯ 1 KÈM 1', en: '1-ON-1 TUTORING' },
        hero_banner2_title_2: { vi: 'GIÚP CON HỌC TIẾN BỘ', en: 'BOOSTING ACADEMIC EXCELLENCE' },
        hero_tag_foundation: { vi: 'CHẮC NỀN TẢNG', en: 'SOLID FOUNDATION' },
        hero_tag_thinking: { vi: 'VỮNG TƯ DUY', en: 'SHARP THINKING' },
        hero_tag_score: { vi: 'NẮM TRỌN ĐIỂM 10', en: 'ACHIEVING TOP SCORES' },
        hero_banner2_desc: { vi: 'Đội ngũ thầy cô và sinh viên xuất sắc từ các trường ĐH hàng đầu (FTU, Bách Khoa, Sư Phạm). Phương pháp dạy kèm 1-1 cá nhân hóa giúp học sinh bứt phá học lực thần tốc!', en: 'Outstanding teachers and students from top universities. Personalized 1-on-1 tutoring methods help students make breakthrough academic progress!' },
        hero_btn_find_tutor: { vi: 'Tìm Gia Sư Cho Con', en: 'Find a Tutor for Child' },
        hero_btn_post_class: { vi: 'Đăng Lớp Cần Gia Sư', en: 'Post Class Request' },
        hero_online_badge: { vi: 'Học Trực Tuyến & Tại Nhà Toàn Quốc', en: 'Online & In-Person Tutoring Nationwide' },
        hero_banner3_title_1: { vi: 'HỌC TẬP THÔNG MINH', en: 'SMART LEARNING' },
        hero_banner3_title_2: { vi: 'TỰ TIN BỨT PHÁ TỎA SÁNG', en: 'CONFIDENT BREAKTHROUGH & SHINE' },
        hero_banner3_desc: { vi: 'Luyện thi vào 10, thi THPT Quốc gia, lấy chứng chỉ IELTS / TOEIC / Tin học quốc tế cùng các gia sư thủ khoa giàu kinh nghiệm và nhiệt huyết.', en: 'Exam preparation for grade 10, High School Graduation, IELTS / TOEIC / international certificates with top-ranking, experienced tutors.' },
        hero_btn_tutor_jobs: { vi: 'Dành Cho Gia Sư Nhận Lớp', en: 'For Tutors Seeking Classes' },
        hero_btn_tutor_reg: { vi: 'Đăng Ký Làm Gia Sư', en: 'Register as a Tutor' },

        // --- Search Modes & Tabs ---
        search_tab_tutors: { vi: 'Dành cho Phụ huynh (Tìm gia sư)', en: 'For Parents (Find Tutors)' },
        search_tab_classes: { vi: 'Dành cho Gia sư (Tìm lớp dạy)', en: 'For Tutors (Find Classes)' },
        search_kw_tutor: { vi: 'Tên gia sư, trường ĐH, từ khóa...', en: 'Tutor name, university, keywords...' },
        search_kw_class: { vi: 'Môn học, khối lớp, tiêu đề lớp...', en: 'Subject, grade, class title...' },
        search_btn: { vi: 'Tìm Kiếm Ngay', en: 'Search Now' },
        search_all_subjects: { vi: '-- Tất cả môn học --', en: '-- All Subjects --' },
        search_all_locations: { vi: '-- Tất cả tỉnh / thành --', en: '-- All Provinces / Cities --' },
        search_all_districts: { vi: '-- Tất cả phường / xã --', en: '-- All Wards / Districts --' },
        search_online_option: { vi: '🌐 Học Online (Toàn quốc)', en: '🌐 Online Learning (Nationwide)' },
        search_major_cities: { vi: 'Thành phố lớn', en: 'Major Cities' },
        search_all_provinces: { vi: 'Tất cả tỉnh thành', en: 'All Provinces' },

        // --- Homepage Highlights & Sections ---
        stat_tutors: { vi: 'Gia sư tuyển chọn', en: 'Selected Tutors' },
        stat_classes: { vi: 'Lớp ghép thành công', en: 'Matched Classes' },
        stat_students: { vi: 'Học sinh & Phụ huynh', en: 'Students & Parents' },
        stat_satisfaction: { vi: 'Hài lòng & Tiến bộ', en: 'Satisfaction & Progress' },
        sec_featured_tutors_title: { vi: 'Gia Sư Tiêu Biểu & Đạt Chuẩn Kiểm Duyệt', en: 'Featured & Verified Tutors' },
        sec_featured_tutors_sub: { vi: 'Hồ sơ lý lịch rõ ràng, bằng cấp xuất sắc từ các trường đại học danh tiếng', en: 'Transparent profiles and outstanding degrees from top universities' },
        sec_latest_classes_title: { vi: 'Lớp Học Mới Đang Cần Gia Sư', en: 'New Classes Looking for Tutors' },
        sec_latest_classes_sub: { vi: 'Các yêu cầu tìm gia sư vừa được phụ huynh đăng tải, mức học phí hấp dẫn', en: 'Latest tutor requests posted by parents with competitive rates' },
        view_all_tutors: { vi: 'Xem tất cả gia sư', en: 'View All Tutors' },
        view_all_classes: { vi: 'Xem tất cả lớp học', en: 'View All Classes' },

        // --- Why Choose TutorLink ---
        why_title: { vi: 'Tại Sao Hơn 10.000+ Phụ Huynh & Gia Sư Chọn TutorLink?', en: 'Why 10,000+ Parents & Tutors Choose TutorLink?' },
        why_verified_title: { vi: 'Kiểm Duyệt Hồ Sơ Nghiêm Ngặt', en: 'Strict Profile Verification' },
        why_verified_desc: { vi: '100% hồ sơ gia sư được thẩm định CCCD, thẻ sinh viên, bằng tốt nghiệp và chứng chỉ ngoại ngữ trước khi phê duyệt.', en: '100% of tutor profiles are verified with national ID, student cards, graduation diplomas, and language certificates.' },
        why_match_title: { vi: 'Ghép Lớp Nhanh & Chính Xác', en: 'Fast & Accurate Matching' },
        why_match_desc: { vi: 'Thuật toán kết nối thông minh theo môn học, khu vực, lịch rảnh và mức thù lao mong muốn chỉ trong vòng vài giờ.', en: 'Smart matching algorithm based on subject, location, availability, and expected rate within hours.' },
        why_rating_title: { vi: 'Đánh Giá Công Khai & Minh Bạch', en: 'Public & Honest Reviews' },
        why_rating_desc: { vi: 'Chỉ học sinh đã hoàn thành khóa học mới có quyền đánh giá điểm sao và viết nhận xét chi tiết.', en: 'Only students who have finished classes can submit star ratings and detailed reviews.' },
        why_support_title: { vi: 'Đổi Gia Sư & Hỗ Trợ 24/7', en: 'Tutor Replacement & 24/7 Support' },
        why_support_desc: { vi: 'Cam kết đổi gia sư miễn phí nếu học sinh không tiến bộ hoặc không hợp phong cách giảng dạy trong 2 buổi đầu.', en: 'Committed to free tutor replacement if students do not show progress in the first 2 sessions.' },

        // --- Workflow Steps ---
        workflow_title: { vi: 'Quy Trình Kết Nối 4 Bước Dễ Dàng', en: 'Simple 4-Step Connection Workflow' },
        step1_title: { vi: '1. Đăng Tin Hoặc Tìm Kiếm', en: '1. Post or Search' },
        step1_desc: { vi: 'Phụ huynh đăng bài cần gia sư hoặc tìm gia sư có sẵn trong danh sách.', en: 'Parents post tutoring requests or browse pre-listed qualified tutors.' },
        step2_title: { vi: '2. Ứng Tuyển & Trao Đổi', en: '2. Apply & Discuss' },
        step2_desc: { vi: 'Gia sư phù hợp gửi hồ sơ ứng tuyển, hai bên trao đổi học phí và lịch học.', en: 'Qualified tutors apply, and both parties discuss schedule and fees.' },
        step3_title: { vi: '3. Ghép Lớp Tự Động', en: '3. Auto Class Match' },
        step3_desc: { vi: 'Phụ huynh duyệt ứng viên, hệ thống tự động khởi tạo lớp học và gửi thông báo.', en: 'Parents approve candidates, and the system automatically matches the class.' },
        step4_title: { vi: '4. Học Tập & Đánh Giá', en: '4. Learn & Review' },
        step4_desc: { vi: 'Tiến hành giảng dạy kèm 1-1, học sinh đánh giá chất lượng sau khóa học.', en: 'Conduct 1-on-1 tutoring, and students review teaching quality upon completion.' },

        // --- Footer ---
        footer_desc: {
            vi: 'Nền tảng kết nối Học sinh, Gia sư và Quản trị viên trực tuyến hiện đại, minh bạch, chất lượng cao. Đồ án xây dựng theo chuẩn mực bài bản và trải nghiệm mượt mà.',
            en: 'Modern, transparent, and high-quality online platform connecting Students, Tutors, and Administrators.'
        },
        footer_badge1: { vi: 'Đồ án Web 5 TV', en: 'Web Project 5 TV' },
        footer_badge2: { vi: 'Hồ sơ kiểm duyệt', en: 'Verified Profiles' },
        footer_for_students: { vi: 'Dành cho Học sinh', en: 'For Students' },
        footer_find_tutor: { vi: 'Tìm gia sư giỏi', en: 'Find Top Tutors' },
        footer_post_request: { vi: 'Đăng tin tìm gia sư', en: 'Post Tutor Request' },
        footer_sample_classes: { vi: 'Xem lớp học mẫu', en: 'Browse Classes' },
        footer_reg_student: { vi: 'Đăng ký học viên', en: 'Register as Student' },
        footer_for_tutors: { vi: 'Dành cho Gia sư', en: 'For Tutors' },
        footer_find_teaching: { vi: 'Tìm lớp nhận dạy', en: 'Find Teaching Jobs' },
        footer_reg_tutor: { vi: 'Đăng ký làm gia sư', en: 'Register as Tutor' },
        footer_ranking: { vi: 'Bảng xếp hạng gia sư', en: 'Tutor Rankings' },
        footer_login_acc: { vi: 'Đăng nhập tài khoản', en: 'Account Login' },
        footer_contact_support: { vi: 'Thông tin liên hệ & Hỗ trợ', en: 'Contact & Support' },
        footer_uni: { vi: 'Trường Đại Học - Khoa CNTT', en: 'University - IT Faculty' },
        footer_support_247: { vi: 'Hỗ trợ kết nối 24/7 trực tuyến', en: '24/7 Online Support' },
        footer_copyright: { vi: 'Tất cả quyền được bảo lưu.', en: 'All rights reserved.' },
        footer_simple: { vi: 'Đơn giản', en: 'Simple' },
        footer_trusted: { vi: 'Uy tín', en: 'Trusted' },
        footer_demo: { vi: 'Dễ demo', en: 'Demo-ready' },

        // --- Authentication (Login & Register) ---
        auth_login_title: { vi: 'Đăng Nhập TutorLink', en: 'Log In to TutorLink' },
        auth_login_sub: { vi: 'Chào mừng bạn quay trở lại nền tảng kết nối gia sư', en: 'Welcome back to the tutor connection platform' },
        auth_username: { vi: 'Tên đăng nhập', en: 'Username' },
        auth_username_placeholder: { vi: 'Nhập tên đăng nhập', en: 'Enter username' },
        auth_password: { vi: 'Mật khẩu', en: 'Password' },
        auth_password_placeholder: { vi: 'Nhập mật khẩu', en: 'Enter password' },
        auth_btn_login: { vi: 'Đăng Nhập', en: 'Log In' },
        auth_no_account: { vi: 'Chưa có tài khoản?', en: "Don't have an account?" },
        auth_register_now: { vi: 'Đăng ký ngay', en: 'Sign up now' },
        auth_demo_title: { vi: 'Tài khoản Demo sẵn có:', en: 'Available Demo Accounts:' },

        auth_register_title: { vi: 'Tạo Tài Khoản Mới', en: 'Create New Account' },
        auth_register_sub: { vi: 'Trở thành thành viên của cộng đồng TutorLink', en: 'Become a member of the TutorLink community' },
        auth_role_question: { vi: 'Bạn muốn tham gia với vai trò gì?', en: 'Which role would you like to register as?' },
        auth_role_student_title: { vi: 'Học sinh / Phụ huynh', en: 'Student / Parent' },
        auth_role_student_desc: { vi: 'Tìm gia sư & đăng tin', en: 'Find tutors & post requests' },
        auth_role_tutor_title: { vi: 'Gia sư', en: 'Tutor' },
        auth_role_tutor_desc: { vi: 'Tìm lớp & dạy học', en: 'Find classes & teach' },
        auth_fullname: { vi: 'Họ và tên', en: 'Full Name' },
        auth_phone: { vi: 'Số điện thoại', en: 'Phone Number' },
        auth_email: { vi: 'Email liên hệ', en: 'Contact Email' },
        auth_confirm_password: { vi: 'Xác nhận mật khẩu', en: 'Confirm Password' },
        auth_btn_register: { vi: 'Hoàn Tất Đăng Ký', en: 'Complete Registration' },
        auth_have_account: { vi: 'Đã có tài khoản?', en: 'Already have an account?' },

        // --- Profile Page & Facebook Avatar Cropper ---
        profile_title: { vi: 'Hồ sơ cá nhân', en: 'Personal Profile' },
        profile_edit_title: { vi: 'Cập Nhật Thông Tin Cá Nhân', en: 'Update Personal Information' },
        profile_edit_sub: { vi: 'Quản lý và chỉnh sửa thông tin tài khoản của bạn', en: 'Manage and update your account details' },
        profile_username_fixed: { vi: 'Tên đăng nhập (Cố định)', en: 'Username (Fixed)' },
        profile_address: { vi: 'Địa chỉ', en: 'Address' },
        profile_bio: { vi: 'Giới thiệu ngắn (Bio)', en: 'Short Bio' },
        profile_avatar: { vi: 'Ảnh đại diện', en: 'Profile Avatar' },
        profile_btn_change_avatar: { vi: 'Đổi ảnh đại diện', en: 'Change Avatar' },
        profile_btn_save: { vi: 'Lưu Thông Tin Cá Nhân', en: 'Save Profile Info' },
        profile_join_date: { vi: 'Tham gia:', en: 'Joined:' },
        profile_avatar_modal_title: { vi: 'Cập nhật ảnh đại diện', en: 'Update Profile Picture' },
        profile_zoom_slider: { vi: 'Thu phóng ảnh', en: 'Zoom' },
        profile_btn_cancel: { vi: 'Hủy', en: 'Cancel' },
        profile_btn_save_avatar: { vi: 'Lưu ảnh đại diện', en: 'Save Avatar' },

        // --- Tutor List & Filter Sidebar ---
        tutors_page_title: { vi: 'Tìm Kiếm Gia Sư Phù Hợp', en: 'Find Qualified Tutors' },
        tutors_filter_title: { vi: 'Bộ Lọc', en: 'Filters' },
        tutors_reset_filter: { vi: 'Đặt lại', en: 'Reset' },
        tutors_keyword_label: { vi: 'Từ khóa / Tên', en: 'Keyword / Name' },
        tutors_keyword_placeholder: { vi: 'Tìm theo tên, môn...', en: 'Search by name, subject...' },
        tutors_subject_label: { vi: 'Môn học', en: 'Subject' },
        tutors_location_label: { vi: 'Tỉnh / Thành phố', en: 'Province / City' },
        tutors_district_label: { vi: 'Phường / Xã', en: 'Ward / District' },
        tutors_method_label: { vi: 'Hình thức giảng dạy', en: 'Teaching Mode' },
        tutors_method_all: { vi: '-- Tất cả hình thức --', en: '-- All Modes --' },
        tutors_method_online: { vi: 'Trực tuyến (Online)', en: 'Online' },
        tutors_method_offline: { vi: 'Trực tiếp (Offline)', en: 'In-Person (Offline)' },
        tutors_method_both: { vi: 'Linh hoạt cả hai', en: 'Flexible (Both)' },
        tutors_price_label: { vi: 'Mức học phí (/giờ)', en: 'Hourly Rate (/hr)' },
        tutors_price_all: { vi: '-- Mọi mức giá --', en: '-- Any Price --' },
        tutors_price_under_150: { vi: 'Dưới 150.000 đ', en: 'Under 150,000 VND' },
        tutors_price_under_200: { vi: 'Dưới 200.000 đ', en: 'Under 200,000 VND' },
        tutors_price_under_300: { vi: 'Dưới 300.000 đ', en: 'Under 300,000 VND' },
        tutors_price_under_500: { vi: 'Dưới 500.000 đ', en: 'Under 500,000 VND' },
        tutors_price_above_500: { vi: 'Trên 500.000 đ', en: 'Above 500,000 VND' },
        tutors_rating_label: { vi: 'Đánh giá tối thiểu', en: 'Minimum Rating' },
        tutors_rating_all: { vi: '-- Mọi đánh giá --', en: '-- Any Rating --' },
        tutors_btn_apply_filter: { vi: 'Áp Dụng Bộ Lọc', en: 'Apply Filters' },
        tutors_card_verified: { vi: 'Đã kiểm duyệt', en: 'Verified' },
        tutors_card_reviews: { vi: 'đánh giá', en: 'reviews' },
        tutors_card_completed_classes: { vi: 'lớp đã hoàn thành', en: 'classes completed' },
        tutors_card_btn_view: { vi: 'Xem Hồ Sơ', en: 'View Profile' },
        tutors_card_btn_request: { vi: 'Gửi yêu cầu học', en: 'Send Study Request' },
        tutors_empty_result: { vi: 'Chưa tìm thấy gia sư phù hợp với tiêu chí lọc.', en: 'No tutors found matching the selected filter criteria.' },

        // --- Tutor Detail Page ---
        tutor_section_banner: { vi: 'THÔNG TIN GIA SƯ', en: 'TUTOR INFORMATION' },
        tutor_sub_basic_info: { vi: 'Thông tin cơ bản', en: 'Basic Information' },
        tutor_birth_year: { vi: 'Năm sinh:', en: 'Birth Year:' },
        tutor_gender: { vi: 'Giới tính:', en: 'Gender:' },
        tutor_hometown: { vi: 'Quê quán:', en: 'Hometown:' },
        tutor_voice: { vi: 'Giọng nói:', en: 'Accent / Voice:' },
        tutor_academic_level: { vi: 'Học vấn:', en: 'Academic Level:' },
        tutor_sub_experience: { vi: 'Kinh nghiệm gia sư, giảng dạy', en: 'Teaching & Tutoring Experience' },
        tutor_sub_achievements: { vi: 'Thành tích trong học tập và dạy học', en: 'Academic & Teaching Achievements' },
        tutor_section_subjects: { vi: 'MÔN HỌC & LỚP DẠY', en: 'SUBJECTS & CLASSES' },
        tutor_subjects_taught: { vi: 'Môn học nhận dạy', en: 'Subjects Offered' },
        tutor_grades_taught: { vi: 'Lớp dạy / Đối tượng', en: 'Target Grades / Levels' },
        tutor_teaching_mode: { vi: 'Hình thức dạy', en: 'Teaching Mode' },
        tutor_section_schedule: { vi: 'LỊCH DẠY CÓ THỂ ĐI DẠY', en: 'AVAILABLE TEACHING SCHEDULE' },
        tutor_schedule_session_day: { vi: 'Buổi / Thứ', en: 'Session / Day' },
        tutor_morning: { vi: 'Sáng', en: 'Morning' },
        tutor_afternoon: { vi: 'Chiều', en: 'Afternoon' },
        tutor_evening: { vi: 'Tối', en: 'Evening' },
        tutor_mon: { vi: 'Thứ 2', en: 'Mon' },
        tutor_tue: { vi: 'Thứ 3', en: 'Tue' },
        tutor_wed: { vi: 'Thứ 4', en: 'Wed' },
        tutor_thu: { vi: 'Thứ 5', en: 'Thu' },
        tutor_fri: { vi: 'Thứ 6', en: 'Fri' },
        tutor_sat: { vi: 'Thứ 7', en: 'Sat' },
        tutor_sun: { vi: 'Chủ Nhật', en: 'Sun' },
        tutor_section_reviews: { vi: 'ĐÁNH GIÁ TỪ HỌC SINH & PHỤ HUYNH', en: 'REVIEWS FROM STUDENTS & PARENTS' },
        tutor_rate_label: { vi: 'Mức học phí:', en: 'Tuition Rate:' },
        tutor_btn_send_request: { vi: 'Gửi Yêu Cầu Học', en: 'Send Study Request' },
        tutor_btn_edit_profile: { vi: 'Chỉnh sửa hồ sơ của bạn', en: 'Edit Your Profile' },
        tutor_btn_login_to_request: { vi: 'Đăng nhập để gửi yêu cầu', en: 'Log in to send request' },

        // --- Class Requests / Class List ---
        classes_page_title: { vi: 'Lớp Học Đang Cần Gia Sư', en: 'Classes Looking for Tutors' },
        classes_page_sub: { vi: 'Các bài đăng tìm gia sư trực tiếp từ học sinh và phụ huynh. Gia sư có thể ứng tuyển ngay!', en: 'Direct tutor requests from students and parents. Tutors can apply immediately!' },
        classes_btn_post: { vi: 'Đăng tin tìm gia sư mới', en: 'Post New Tutor Request' },
        classes_filter_title: { vi: 'Bộ Lọc Lớp', en: 'Class Filters' },
        classes_grade_label: { vi: 'Khối lớp / Trình độ', en: 'Grade / Level' },
        classes_grade_placeholder: { vi: 'VD: Lớp 10, Lớp 12...', en: 'e.g., Grade 10, Grade 12...' },
        classes_btn_filter: { vi: 'Lọc Lớp Học', en: 'Filter Classes' },
        classes_card_student: { vi: 'Học sinh:', en: 'Student:' },
        classes_card_budget: { vi: 'Học phí đề xuất:', en: 'Proposed rate:' },
        classes_card_session: { vi: '/ buổi', en: '/ session' },
        classes_card_free_time: { vi: 'Thời gian rảnh:', en: 'Available time:' },
        classes_card_location: { vi: 'Địa điểm:', en: 'Location:' },
        classes_card_posted_on: { vi: 'Ngày đăng:', en: 'Posted on:' },
        classes_card_btn_detail: { vi: 'Xem chi tiết & Ứng tuyển', en: 'View Details & Apply' },
        classes_empty_result: { vi: 'Chưa có bài đăng nào phù hợp.', en: 'No matching class requests found.' },

        // --- Post Class Request Form ---
        post_class_title: { vi: 'Đăng Yêu Cầu Tìm Gia Sư Mới', en: 'Post a New Tutor Request' },
        post_class_edit_title: { vi: 'Chỉnh Sửa Bài Đăng Tìm Gia Sư', en: 'Edit Tutor Request' },
        post_class_sub: { vi: 'Điền đầy đủ thông tin để nhận được phản hồi nhanh và chính xác nhất từ các gia sư', en: 'Provide detailed information to receive fast and accurate responses from tutors' },
        post_class_field_title: { vi: 'Tiêu đề bài đăng', en: 'Request Title' },
        post_class_field_subject: { vi: 'Môn học', en: 'Subject' },
        post_class_field_grade: { vi: 'Khối lớp / Trình độ', en: 'Grade / Level' },
        post_class_field_method: { vi: 'Hình thức dạy', en: 'Teaching Mode' },
        post_class_field_budget: { vi: 'Học phí đề xuất (/buổi)', en: 'Proposed Budget (/session)' },
        post_class_field_province: { vi: 'Tỉnh / Thành phố', en: 'Province / City' },
        post_class_field_district: { vi: 'Phường / Xã', en: 'Ward / District' },
        post_class_field_address: { vi: 'Địa chỉ chi tiết', en: 'Specific Address' },
        post_class_field_schedule: { vi: 'Thời gian rảnh / Lịch học', en: 'Available Schedule / Timetable' },
        post_class_field_desc: { vi: 'Mô tả chi tiết & Yêu cầu gia sư', en: 'Detailed Description & Requirements' },
        post_class_btn_submit: { vi: 'Đăng Yêu Cầu Tìm Gia Sư', en: 'Publish Tutor Request' },
        post_class_btn_save_changes: { vi: 'Lưu Thay Đổi', en: 'Save Changes' },

        // --- Class Detail Page ---
        class_detail_req_content: { vi: 'Nội Dung Yêu Cầu Chi Tiết', en: 'Detailed Request Content' },
        class_detail_proposed_rate: { vi: 'Thù lao đề xuất:', en: 'Proposed rate:' },
        class_detail_edit_btn: { vi: 'Sửa tin', en: 'Edit Post' },
        class_detail_close_btn: { vi: 'Đóng bài', en: 'Close Post' },
        class_detail_delete_btn: { vi: 'Xóa', en: 'Delete' },
        class_detail_apply_btn: { vi: 'Ứng Tuyển Nhận Lớp', en: 'Apply for Class' },
        class_detail_applied_notice: { vi: 'Bạn đã ứng tuyển lớp này.', en: 'You have applied for this class.' },
        class_detail_status_label: { vi: 'Trạng thái:', en: 'Status:' },
        class_detail_applications_title: { vi: 'Danh Sách Gia Sư Ứng Tuyển', en: 'List of Applicant Tutors' },
        class_detail_accept_btn: { vi: 'Chấp Nhận Gia Sư', en: 'Accept Tutor' },
        class_detail_reject_btn: { vi: 'Từ Chối', en: 'Decline' },

        // --- Dashboards ---
        dash_student_title: { vi: 'Bảng Điều Khiển Học Sinh', en: 'Student Dashboard' },
        dash_tutor_title: { vi: 'Bảng Điều Khiển Gia Sư', en: 'Tutor Dashboard' },
        dash_admin_title: { vi: 'Bảng Điều Khiển Quản Trị Viên', en: 'Admin Dashboard' },
        dash_stat_posts: { vi: 'Bài đăng tìm gia sư', en: 'Tutor Requests' },
        dash_stat_active_classes: { vi: 'Lớp đang học', en: 'Active Classes' },
        dash_stat_completed_classes: { vi: 'Lớp đã hoàn thành', en: 'Completed Classes' },
        dash_stat_sent_requests: { vi: 'Yêu cầu trực tiếp', en: 'Direct Requests' },
        dash_stat_teaching_classes: { vi: 'Lớp đang giảng dạy', en: 'Teaching Classes' },
        dash_stat_applied: { vi: 'Lớp đã ứng tuyển', en: 'Applied Classes' },
        dash_stat_received_requests: { vi: 'Yêu cầu học nhận được', en: 'Received Requests' },
        dash_active_classes_section: { vi: 'Lớp Đang Học', en: 'Active Classes' },
        dash_recent_posts_section: { vi: 'Bài Đăng Mới Nhất', en: 'Recent Requests' },
        dash_enter_class_btn: { vi: 'Vào lớp', en: 'Enter Class' },
        dash_view_all: { vi: 'Xem tất cả', en: 'View All' },
        dash_empty_active_classes: { vi: 'Chưa có lớp học nào đang diễn ra.', en: 'No ongoing classes yet.' },

        // --- Matched Classes ---
        matched_page_title: { vi: 'Lớp Học Của Tôi', en: 'My Classes' },
        matched_page_sub: { vi: 'Theo dõi tiến độ, thông tin liên lạc và đánh giá các lớp học của bạn', en: 'Track progress, contact details, and reviews of your classes' },
        matched_th_subject: { vi: 'Môn học', en: 'Subject' },
        matched_th_tutor: { vi: 'Gia sư giảng dạy', en: 'Tutor' },
        matched_th_student: { vi: 'Học sinh', en: 'Student' },
        matched_th_schedule: { vi: 'Lịch học', en: 'Schedule' },
        matched_th_rate: { vi: 'Học phí', en: 'Rate' },
        matched_th_status: { vi: 'Trạng thái', en: 'Status' },
        matched_th_review: { vi: 'Đánh giá', en: 'Review' },
        matched_th_action: { vi: 'Chi tiết', en: 'Details' },
        matched_btn_review: { vi: 'Đánh giá', en: 'Leave Review' },
        matched_waiting_completion: { vi: 'Chờ hoàn thành', en: 'Pending Completion' },
        matched_empty: { vi: 'Chưa có lớp học nào.', en: 'No classes matched yet.' },

        // --- Reviews ---
        review_page_title: { vi: 'Đánh Giá Gia Sư', en: 'Review Tutor' },
        review_page_sub: { vi: 'Cảm nhận và đóng góp chân thực của bạn giúp nâng cao chất lượng kết nối của cộng đồng', en: 'Your authentic feedback helps enhance connection quality in the community' },
        review_rating_label: { vi: 'Mức độ hài lòng của bạn', en: 'Your Satisfaction Rating' },
        review_comment_label: { vi: 'Nhận xét chi tiết', en: 'Detailed Review Comments' },
        review_comment_placeholder: { vi: 'VD: Thầy cô dạy rất dễ hiểu, đúng giờ và nhiệt tình giải đáp bài tập.', en: 'e.g., The tutor explained concepts clearly, was punctual and very helpful.' },
        review_btn_back: { vi: 'Quay lại', en: 'Go Back' },
        review_btn_submit: { vi: 'Gửi Đánh Giá Ngay', en: 'Submit Review Now' },

        // --- Status Badges & Generic Terms ---
        status_pending: { vi: 'Chờ duyệt', en: 'Pending Approval' },
        status_approved: { vi: 'Đã duyệt', en: 'Approved' },
        status_rejected: { vi: 'Từ chối', en: 'Rejected' },
        status_open: { vi: 'Đang mở', en: 'Open' },
        status_accepted: { vi: 'Đã nhận', en: 'Accepted' },
        status_closed: { vi: 'Đã đóng', en: 'Closed' },
        status_in_progress: { vi: 'Đang học', en: 'In Progress' },
        status_completed: { vi: 'Đã hoàn thành', en: 'Completed' },
        status_cancelled: { vi: 'Đã hủy', en: 'Cancelled' },
        status_online: { vi: 'Trực tuyến', en: 'Online' },
        status_offline: { vi: 'Trực tiếp tại nhà', en: 'In-person at home' },
        status_flexible: { vi: 'Linh hoạt', en: 'Flexible' },

        // --- Common Actions ---
        btn_save: { vi: 'Lưu', en: 'Save' },
        btn_cancel: { vi: 'Hủy bỏ', en: 'Cancel' },
        btn_close: { vi: 'Đóng', en: 'Close' },
        btn_confirm: { vi: 'Xác nhận', en: 'Confirm' },
        btn_delete: { vi: 'Xóa', en: 'Delete' },
        btn_edit: { vi: 'Chỉnh sửa', en: 'Edit' },
        btn_back: { vi: 'Quay lại', en: 'Back' },
        btn_details: { vi: 'Chi tiết', en: 'Details' },
        btn_apply: { vi: 'Ứng tuyển', en: 'Apply' },
        btn_send: { vi: 'Gửi', en: 'Send' },

        // --- AI Virtual Assistant Widget ---
        ai_assistant_title: { vi: 'Trợ Lý AI TutorLink', en: 'TutorLink AI Assistant' },
        ai_assistant_sub: { vi: 'Trợ lý ảo sẵn sàng hỗ trợ 24/7', en: 'Virtual assistant ready 24/7' },
        ai_assistant_welcome_greeting: { vi: 'Chào bạn', en: 'Hello' },
        ai_assistant_welcome_sub: { vi: 'Trợ lý AI TutorLink 🎓', en: 'TutorLink AI Assistant 🎓' },
        ai_assistant_welcome_msg: {
            vi: 'Mình có thể hỗ trợ bạn tìm gia sư giỏi, tìm lớp dạy phù hợp, hướng dẫn đăng tin hoặc tra cứu học phí nhanh chóng! Bạn đang cần hỗ trợ gì?',
            en: 'I can help you find qualified tutors, search for teaching classes, guide you to post requests, or check rates quickly! How may I assist you today?'
        },
        ai_assistant_quick_title: { vi: 'Chọn nhanh câu hỏi bạn quan tâm:', en: 'Quick questions you might ask:' },
        ai_assistant_topic_find_classes: { vi: '📚 Tìm lớp gia sư?', en: '📚 Find tutoring jobs?' },
        ai_assistant_topic_find_tutors: { vi: '🔍 Tìm gia sư giỏi?', en: '🔍 Find top tutors?' },
        ai_assistant_topic_post_class: { vi: '📝 Đăng tin tìm gia sư?', en: '📝 Post tutor request?' },
        ai_assistant_topic_tuition: { vi: '💰 Mức học phí?', en: '💰 Tutoring rates?' },
        ai_assistant_topic_workflow: { vi: '⚡ Quy trình ghép lớp?', en: '⚡ Matching process?' },
        ai_assistant_topic_hotline: { vi: '📞 Hotline hỗ trợ?', en: '📞 Support hotline?' },
        ai_assistant_input_placeholder: { vi: 'Nhập câu hỏi cho AI...', en: 'Ask a question to AI...' },
        ai_assistant_round_tag: { vi: 'Hỏi Trợ Lý', en: 'Ask AI' },
        ai_assistant_toggle_title: { vi: 'Hỏi Trợ Lý AI TutorLink (Nhấp để trò chuyện / Kéo để di chuyển)', en: 'Ask TutorLink AI Assistant (Click to chat / Drag to reposition)' }
    };

    // 2. TỪ ĐIỂN ÁNH XẠ CỤM TỪ TRỰC TIẾP (Direct Text Node Phrase Mapping)
    const PHRASE_MAP = [
        // Navigation & Menu
        { vi: 'Trang chủ', en: 'Home' },
        { vi: 'Dành cho Phụ huynh', en: 'For Parents' },
        { vi: 'Dành cho Gia sư', en: 'For Tutors' },
        { vi: 'Đăng Tìm Gia Sư', en: 'Post Request' },
        { vi: 'Đăng tin tìm gia sư', en: 'Post Tutor Request' },
        { vi: 'Đăng tin cần gia sư', en: 'Post Tutor Request' },
        { vi: 'Đăng tìm gia sư mới', en: 'Post New Request' },
        { vi: 'Đăng tìm gia sư', en: 'Post Tutor Request' },
        { vi: 'Tìm gia sư', en: 'Find Tutors' },
        { vi: 'Tìm Gia Sư Cho Con', en: 'Find Tutor For Child' },
        { vi: 'Đăng Lớp Cần Gia Sư', en: 'Post Class Request' },
        { vi: 'Dành Cho Gia Sư Nhận Lớp', en: 'For Tutors Seeking Classes' },
        { vi: 'Đăng Ký Làm Gia Sư', en: 'Register as Tutor' },
        { vi: 'Bảng điều khiển', en: 'Dashboard' },
        { vi: 'Bài đăng của tôi', en: 'My Posts' },
        { vi: 'Yêu cầu học', en: 'Study Requests' },
        { vi: 'Yêu cầu học đã gửi', en: 'Sent Study Requests' },
        { vi: 'Yêu Cầu Học Đã Gửi', en: 'Sent Study Requests' },
        { vi: 'Yêu Cầu Học Đến', en: 'Received Study Requests' },
        { vi: 'Quản Trị Viên', en: 'Admin Portal' },
        { vi: 'TRANG QUẢN TRỊ', en: 'ADMIN CONTROL PANEL' },
        { vi: 'Admin Control Center', en: 'Admin Control Center' },
        { vi: 'Tổng quan', en: 'Overview' },
        { vi: 'Tổng Quan Hệ Thống', en: 'System Overview' },
        { vi: 'Quản lý Tài khoản', en: 'User Management' },
        { vi: 'Quản Lý Tài Khoản Người Dùng', en: 'User Account Management' },
        { vi: 'Duyệt Gia Sư', en: 'Tutor Approvals' },
        { vi: 'Kiểm Duyệt Hồ Sơ Gia Sư', en: 'Tutor Profile Approvals' },
        { vi: 'Quản lý Bài Đăng', en: 'Post Management' },
        { vi: 'Quản Lý Yêu Cầu Tìm Gia Sư', en: 'Manage Tutor Requests' },
        { vi: 'Quản lý Lớp Ghép', en: 'Matched Classes' },
        { vi: 'Quản Lý Lớp Học Đã Ghép', en: 'Manage Matched Classes' },
        { vi: 'Quản lý Đánh Giá', en: 'Review Management' },
        { vi: 'Quản Lý Đánh Giá & Nhận Xét', en: 'Manage Reviews & Feedback' },
        { vi: 'Báo Cáo Thống Kê', en: 'Statistics & Reports' },
        { vi: 'Báo Cáo & Thống Kê Chi Tiết', en: 'Detailed Reports & Statistics' },
        { vi: 'Django Admin', en: 'Django Admin' },

        // Admin Sub-descriptions & Table headers
        { vi: 'Theo dõi toàn bộ số liệu và hoạt động trên TutorLink theo thời gian thực', en: 'Monitor all metrics and activities on TutorLink in real-time' },
        { vi: 'Xem danh sách, phân quyền và khóa/mở khóa tài khoản khi cần', en: 'View list, manage permissions, and lock/unlock accounts' },
        { vi: 'Xem xét trình độ, bằng cấp, kinh nghiệm và quyết định phê duyệt gia sư', en: 'Review qualifications, diplomas, experience and approve tutors' },
        { vi: 'Giám sát các tin đăng tìm gia sư trên toàn hệ thống', en: 'Monitor tutor requests across the entire system' },
        { vi: 'Theo dõi tiến độ tất cả các lớp học được kết nối trên nền tảng', en: 'Track progress of all matched classes across the platform' },
        { vi: 'Kiểm tra phản hồi của học sinh, xử lý hoặc xóa các đánh giá không chuẩn mực', en: 'Check student reviews, moderate or remove inappropriate feedback' },
        { vi: 'Các chỉ số định lượng về tốc độ phát triển và hiệu quả kết nối', en: 'Quantitative indicators on growth and matching efficiency' },
        { vi: 'Người dùng', en: 'Users' },
        { vi: 'Học sinh', en: 'Students' },
        { vi: 'Gia sư', en: 'Tutors' },
        { vi: 'Chờ duyệt', en: 'Pending Approval' },
        { vi: 'Bài đăng tìm', en: 'Tutor Requests' },
        { vi: 'Lớp đã ghép', en: 'Matched Classes' },
        { vi: 'Hồ Sơ Gia Sư Chờ Duyệt', en: 'Pending Tutor Profiles' },
        { vi: 'Yêu Cầu Tìm Gia Sư Mới', en: 'New Tutor Requests' },
        { vi: 'Xét duyệt', en: 'Review' },
        { vi: 'Không có hồ sơ nào đang chờ duyệt.', en: 'No tutor profiles pending approval.' },
        { vi: 'Chưa có bài đăng nào.', en: 'No posts available.' },
        { vi: 'Tài khoản', en: 'Account' },
        { vi: 'Email', en: 'Email' },
        { vi: 'Vai trò', en: 'Role' },
        { vi: 'Số điện thoại', en: 'Phone Number' },
        { vi: 'Trạng thái', en: 'Status' },
        { vi: 'Ngày tham gia', en: 'Joined Date' },
        { vi: 'Hành động', en: 'Actions' },
        { vi: 'Chưa có email', en: 'No email' },
        { vi: 'Đang bị khóa', en: 'Locked' },
        { vi: 'Hoạt động', en: 'Active' },
        { vi: 'Mở khóa', en: 'Unlock' },
        { vi: 'Khóa nick', en: 'Lock Account' },
        { vi: 'Không có người dùng nào.', en: 'No users found.' },
        { vi: 'Bị từ chối', en: 'Rejected' },
        { vi: 'Chưa có sđt', en: 'No phone' },
        { vi: 'Học vấn / Bằng cấp:', en: 'Education / Degree:' },
        { vi: 'Kinh nghiệm:', en: 'Experience:' },
        { vi: 'Ghi chú phản hồi cho gia sư...', en: 'Feedback note for tutor...' },
        { vi: 'Xem trang', en: 'View Page' },
        { vi: 'Duyệt', en: 'Approve' },
        { vi: 'Từ chối', en: 'Reject' },
        { vi: 'Không có gia sư nào trong danh sách bộ lọc này.', en: 'No tutors found in this filter list.' },
        { vi: 'Học sinh đăng', en: 'Posted By' },
        { vi: 'Môn & Lớp', en: 'Subject & Grade' },
        { vi: 'Ngân sách', en: 'Budget' },
        { vi: 'Xem tin', en: 'View Post' },
        { vi: 'Bắt đầu', en: 'Start Date' },
        { vi: 'Xem lớp', en: 'View Class' },
        { vi: 'Chưa có lớp học nào được ghép.', en: 'No matched classes yet.' },
        { vi: 'Đánh giá gia sư:', en: 'Reviewed Tutor:' },
        { vi: 'Xóa đánh giá', en: 'Delete Review' },
        { vi: 'Chưa có đánh giá nào trên hệ thống.', en: 'No reviews found on system.' },
        { vi: 'Tỷ lệ Gia sư được duyệt', en: 'Tutor Approval Rate' },
        { vi: 'Tỷ lệ Lớp hoàn thành', en: 'Class Completion Rate' },
        { vi: 'Tổng Lượt Ứng Tuyển & Yêu Cầu', en: 'Total Applications & Requests' },
        { vi: 'Hoạt động tương tác 2 chiều', en: '2-way interactive activities' },
        { vi: 'Danh Sách Môn Học Trong Hệ Thống', en: 'Subjects List in System' },
        { vi: 'Tên môn', en: 'Subject Name' },
        { vi: 'Icon', en: 'Icon' },
        { vi: 'Gia sư dạy môn này', en: 'Tutors Teaching Subject' },
        { vi: 'Bài đăng tìm gia sư', en: 'Tutor Requests' },
        { vi: 'Chưa có môn học nào.', en: 'No subjects found.' },

        // User dropdown & Settings
        { vi: 'Thông báo', en: 'Notifications' },
        { vi: 'Đánh dấu đã đọc', en: 'Mark all as read' },
        { vi: 'Tất cả', en: 'All' },
        { vi: 'Chưa đọc', en: 'Unread' },
        { vi: 'Không có thông báo mới', en: 'No new notifications' },
        { vi: 'Thông tin cá nhân', en: 'My Profile' },
        { vi: 'Cập nhật hồ sơ gia sư', en: 'Edit Tutor Profile' },
        { vi: 'Chỉnh sửa hồ sơ gia sư', en: 'Edit Tutor Profile' },
        { vi: 'Chỉnh sửa hồ sơ của bạn', en: 'Edit Your Profile' },
        { vi: 'Lớp học của tôi', en: 'My Classes' },
        { vi: 'Lớp Học Của Tôi', en: 'My Classes' },
        { vi: 'Lớp đã ứng tuyển', en: 'Applied Classes' },
        { vi: 'Lớp Đã Ứng Tuyển', en: 'Applied Classes' },
        { vi: 'Cài đặt hệ thống', en: 'System Settings' },
        { vi: 'Giao diện', en: 'Theme' },
        { vi: 'Sáng', en: 'Light' },
        { vi: 'Tối', en: 'Dark' },
        { vi: 'Ngôn ngữ', en: 'Language' },
        { vi: 'Tiếng Việt', en: 'Vietnamese' },
        { vi: 'Tiếng Anh', en: 'English' },
        { vi: 'Đăng xuất', en: 'Log Out' },
        { vi: 'Đăng nhập', en: 'Log In' },
        { vi: 'Đăng ký', en: 'Sign Up' },
        { vi: 'HỌC SINH', en: 'STUDENT' },
        { vi: 'GIA SƯ', en: 'TUTOR' },
        { vi: 'QUẢN TRỊ VIÊN', en: 'ADMIN' },

        // Dashboards
        { vi: 'Bảng Điều Khiển Học Sinh', en: 'Student Dashboard' },
        { vi: 'Bảng Điều Khiển Gia Sư', en: 'Tutor Dashboard' },
        { vi: 'Quản lý yêu cầu học và lớp học của bạn tại đây.', en: 'Manage your study requests and classes here.' },
        { vi: 'Lớp đang học', en: 'Active Classes' },
        { vi: 'Lớp Đang Học', en: 'Active Classes' },
        { vi: 'Lớp đã hoàn thành', en: 'Completed Classes' },
        { vi: 'Yêu cầu trực tiếp', en: 'Direct Requests' },
        { vi: 'Gia Sư Chờ Bạn Duyệt Nhận Lớp', en: 'Tutors Waiting for Your Approval' },
        { vi: 'Quản lý bài đăng', en: 'Manage Requests' },
        { vi: 'Duyệt & Ghép Lớp', en: 'Approve & Match Class' },
        { vi: 'Không có lượt ứng tuyển mới nào cần duyệt.', en: 'No new applications pending approval.' },
        { vi: 'Dashboard Gia Sư', en: 'Tutor Dashboard' },
        { vi: 'Tìm lớp nhận dạy', en: 'Find Teaching Jobs' },
        { vi: 'Cập nhật hồ sơ', en: 'Update Profile' },
        { vi: 'Hồ sơ gia sư của bạn chưa hoàn thiện', en: 'Your tutor profile is incomplete' },
        { vi: 'Vui lòng cập nhật đầy đủ thông tin cá nhân, môn dạy và học vấn để Ban Quản Trị phê duyệt kích hoạt quyền ứng tuyển nhận lớp.', en: 'Please complete your personal info, subjects, and education for Admin approval to apply for classes.' },
        { vi: 'Cập nhật hồ sơ ngay', en: 'Update Profile Now' },
        { vi: 'Hồ sơ đang chờ Ban Quản Trị phê duyệt', en: 'Profile is pending Admin approval' },
        { vi: 'Hồ sơ của bạn đã hoàn tất và đang được Admin xét duyệt. Bạn sẽ có thể ứng tuyển nhận lớp ngay khi được phê duyệt thành công.', en: 'Your profile is complete and under Admin review. You will be able to apply as soon as approved.' },
        { vi: 'Xem lại hồ sơ', en: 'Review Profile' },
        { vi: 'Hồ sơ chưa được phê duyệt', en: 'Profile not approved yet' },
        { vi: 'Vui lòng cập nhật lại thông tin hồ sơ theo phản hồi từ Admin để được xét duyệt lại.', en: 'Please update your profile information according to Admin feedback to request re-approval.' },
        { vi: 'Cập nhật lại', en: 'Update Again' },
        { vi: 'Yêu cầu học đến', en: 'Incoming Requests' },
        { vi: 'Lớp đang dạy', en: 'Teaching Classes' },
        { vi: 'Đánh giá trung bình', en: 'Average Rating' },
        { vi: 'Yêu Cầu Học Đang Chờ', en: 'Pending Study Requests' },
        { vi: 'Phản hồi', en: 'Respond' },
        { vi: 'Chưa có yêu cầu học trực tiếp nào đang chờ.', en: 'No direct study requests pending.' },
        { vi: 'Lớp Học Đang Diễn Ra', en: 'Ongoing Classes' },
        { vi: 'Quản lý', en: 'Manage' },
        { vi: 'Hiện chưa có lớp học nào đang diễn ra.', en: 'No classes currently in progress.' },

        // Tutor Profile Sidebar & Edit
        { vi: 'Quản lý chung', en: 'Overview' },
        { vi: 'Tìm lớp mới', en: 'Browse Classes' },
        { vi: 'Đơn ứng tuyển', en: 'My Applications' },
        { vi: 'Hồ sơ công khai', en: 'Public Profile' },
        { vi: 'Cài đặt hồ sơ', en: 'Profile Settings' },
        { vi: 'Chào mừng bạn tham gia cộng đồng gia sư TutorLink Việt Nam!', en: 'Welcome to the TutorLink Vietnam tutoring community!' },
        { vi: 'THÔNG TIN CÁ NHÂN', en: 'PERSONAL INFORMATION' },
        { vi: 'Họ tên đầy đủ', en: 'Full Name' },
        { vi: 'Giới tính gia sư', en: 'Tutor Gender' },
        { vi: 'Quê quán', en: 'Hometown' },
        { vi: 'Ngày sinh', en: 'Date of Birth' },
        { vi: 'Giọng nói', en: 'Accent / Voice' },
        { vi: 'Kết nối Facebook của bạn', en: 'Your Facebook Link' },
        { vi: 'Tỉnh/thành (Địa điểm dạy)', en: 'Province / City (Teaching Area)' },
        { vi: 'Địa chỉ hiện tại', en: 'Current Address' },
        { vi: 'THÔNG TIN GIA SƯ', en: 'TUTOR INFORMATION' },
        { vi: 'Kinh nghiệm đi gia sư và giảng dạy (chi tiết)', en: 'Tutoring & Teaching Experience (Details)' },
        { vi: 'Thành tích học tập và dạy học (chi tiết)', en: 'Academic & Teaching Achievements (Details)' },
        { vi: 'HỒ SƠ CHUYÊN MÔN', en: 'PROFESSIONAL PROFILE' },
        { vi: 'Bạn đang là', en: 'You are currently' },
        { vi: 'Trường đang học / đã tốt nghiệp', en: 'University / Graduated School' },
        { vi: 'Sinh viên năm', en: 'Student Year' },
        { vi: 'Chuyên ngành', en: 'Major' },
        { vi: 'Bậc học', en: 'Academic Level' },
        { vi: 'Môn học sẽ dạy', en: 'Subjects to Teach' },
        { vi: 'Chọn tối đa 3 môn', en: 'Select up to 3 subjects' },
        { vi: 'Chủ đề môn dạy (phân cách bằng dấu phẩy)', en: 'Teaching Topics (comma-separated)' },
        { vi: 'Số lượng lớp đã dạy', en: 'Taught Classes Count' },
        { vi: 'Thời gian có thể dạy', en: 'Available Teaching Schedule' },
        { vi: 'ẢNH XÁC NHẬN THÔNG TIN GIA SƯ', en: 'VERIFICATION DOCUMENTS & PHOTOS' },
        { vi: 'Ảnh đại diện (chụp một mình, nhìn rõ mặt)', en: 'Profile Avatar (single photo, clear face)' },
        { vi: 'Chọn ảnh đại diện', en: 'Choose Avatar' },
        { vi: 'Ảnh CMT/Căn cước/Hộ chiếu (Mặt trước)', en: 'National ID / Passport (Front Side)' },
        { vi: 'Tải ảnh CCCD / CMT', en: 'Upload National ID' },
        { vi: 'Thẻ sinh viên/bằng/chứng chỉ (tối đa 3 ảnh)', en: 'Student Card / Diplomas / Certificates (up to 3 photos)' },
        { vi: 'Tải Thẻ SV / Bằng 1', en: 'Upload Student Card / Degree 1' },
        { vi: 'Thẻ sinh viên/bằng/chứng chỉ 2 & 3', en: 'Student Card / Degree 2 & 3' },
        { vi: 'Tải ảnh 2', en: 'Upload Photo 2' },
        { vi: 'Tải ảnh 3', en: 'Upload Photo 3' },
        { vi: 'ẢNH HOẠT ĐỘNG DẠY HỌC VÀ BẢNG THÀNH TÍCH', en: 'TEACHING ACTIVITIES & ACHIEVEMENTS PHOTOS' },
        { vi: 'Tải lên các tệp minh chứng hoạt động dạy học, bài tập học sinh, chứng nhận giải thưởng:', en: 'Upload evidence of teaching activities, student work, award certificates:' },
        { vi: 'Các tệp minh chứng đã lưu:', en: 'Saved verification files:' },
        { vi: 'Xem tệp', en: 'View File' },
        { vi: 'Xóa tệp', en: 'Delete File' },
        { vi: 'Lưu & Cập Nhật Hồ Sơ Gia Sư', en: 'Save & Update Tutor Profile' },
        { vi: 'Xem giao diện hiển thị công khai của hồ sơ', en: 'View public profile page' },

        // Search & Filters
        { vi: 'Dành cho Phụ huynh (Tìm gia sư)', en: 'For Parents (Find Tutors)' },
        { vi: 'Dành cho Gia sư (Tìm lớp dạy)', en: 'For Tutors (Find Classes)' },
        { vi: 'Lớp Học Đang Cần Gia Sư', en: 'Classes In Need Of Tutors' },
        { vi: 'Tìm Kiếm Gia Sư Phù Hợp', en: 'Find Qualified Tutors' },
        { vi: 'Bộ Lọc', en: 'Filters' },
        { vi: 'Bộ Lọc Lớp', en: 'Class Filters' },
        { vi: 'Đặt lại', en: 'Reset' },
        { vi: 'Từ khóa', en: 'Keyword' },
        { vi: 'Từ khóa / Tên', en: 'Keyword / Name' },
        { vi: 'Môn học', en: 'Subject' },
        { vi: '-- Tất cả môn học --', en: '-- All Subjects --' },
        { vi: 'Khối lớp / Trình độ', en: 'Grade / Level' },
        { vi: 'Tỉnh / Thành phố', en: 'Province / City' },
        { vi: '-- Tất cả tỉnh / thành --', en: '-- All Provinces / Cities --' },
        { vi: 'Phường / Xã', en: 'Ward / District' },
        { vi: '-- Tất cả phường / xã --', en: '-- All Wards / Districts --' },
        { vi: 'Hình thức học', en: 'Study Mode' },
        { vi: 'Hình thức giảng dạy', en: 'Teaching Mode' },
        { vi: 'Hình thức dạy', en: 'Teaching Mode' },
        { vi: '-- Tất cả hình thức --', en: '-- All Modes --' },
        { vi: 'Trực tuyến (Online)', en: 'Online' },
        { vi: 'Trực tiếp (Offline)', en: 'In-Person (Offline)' },
        { vi: 'Trực tiếp tại nhà (Offline)', en: 'In-Person (Home)' },
        { vi: 'Linh hoạt cả hai', en: 'Flexible (Both)' },
        { vi: 'Linh hoạt', en: 'Flexible' },
        { vi: 'Mức học phí (/giờ)', en: 'Hourly Rate (/hr)' },
        { vi: 'Mức học phí', en: 'Tuition Rate' },
        { vi: 'Mọi mức giá', en: 'Any Price' },
        { vi: '-- Mọi mức giá --', en: '-- Any Price --' },
        { vi: 'Dưới 150.000 đ', en: 'Under 150,000 VND' },
        { vi: 'Dưới 200.000 đ', en: 'Under 200,000 VND' },
        { vi: 'Dưới 300.000 đ', en: 'Under 300,000 VND' },
        { vi: 'Dưới 500.000 đ', en: 'Under 500,000 VND' },
        { vi: 'Trên 500.000 đ', en: 'Above 500,000 VND' },
        { vi: 'Đánh giá tối thiểu', en: 'Minimum Rating' },
        { vi: '-- Mọi đánh giá --', en: '-- Any Rating --' },
        { vi: 'Áp Dụng Bộ Lọc', en: 'Apply Filters' },
        { vi: 'Lọc Lớp Học', en: 'Filter Classes' },
        { vi: 'Tìm Kiếm Ngay', en: 'Search Now' },

        // Cards & Details
        { vi: 'Xem Hồ Sơ', en: 'View Profile' },
        { vi: 'Xem chi tiết & Ứng tuyển', en: 'View Details & Apply' },
        { vi: 'Xem chi tiết', en: 'View Details' },
        { vi: 'Gửi Yêu Cầu Học', en: 'Send Study Request' },
        { vi: 'Gửi yêu cầu học', en: 'Send study request' },
        { vi: 'Ứng Tuyển Nhận Lớp', en: 'Apply For Class' },
        { vi: 'Vào lớp', en: 'Enter Class' },
        { vi: 'Xem tất cả', en: 'View All' },
        { vi: 'Đã kiểm duyệt', en: 'Verified' },
        { vi: 'Chưa kiểm duyệt', en: 'Unverified' },
        { vi: 'Chờ duyệt', en: 'Pending Approval' },
        { vi: 'Đã duyệt', en: 'Approved' },
        { vi: 'Từ chối', en: 'Rejected' },
        { vi: 'Đang mở', en: 'Open' },
        { vi: 'Đã nhận', en: 'Matched' },
        { vi: 'Đang học', en: 'In Progress' },
        { vi: 'Hoàn thành', en: 'Completed' },
        { vi: 'Đã hoàn thành', en: 'Completed' },
        { vi: 'Đã đóng', en: 'Closed' },
        { vi: 'Đã hủy', en: 'Cancelled' },
        { vi: 'Thù lao đề xuất:', en: 'Proposed rate:' },
        { vi: 'Học phí đề xuất:', en: 'Proposed rate:' },
        { vi: 'Thời gian rảnh:', en: 'Available schedule:' },
        { vi: 'Địa điểm:', en: 'Location:' },
        { vi: 'Ngày đăng:', en: 'Posted date:' },
        { vi: 'Học sinh:', en: 'Student:' },
        { vi: 'Gia sư:', en: 'Tutor:' },
        { vi: 'Lịch học:', en: 'Schedule:' },
        { vi: 'Trạng thái:', en: 'Status:' },
        { vi: 'Đánh giá:', en: 'Review:' },
        { vi: 'Học phí cơ bản:', en: 'Base tuition:' },
        { vi: 'Gửi yêu cầu trực tiếp', en: 'Direct Study Request' },
        { vi: 'Chờ hoàn thành', en: 'Pending completion' },
        { vi: 'Thỏa thuận trực tiếp', en: 'Direct arrangement' },
        { vi: 'Chưa có bài đăng nào phù hợp.', en: 'No matching class requests found.' },
        { vi: 'Chưa có lớp học nào đang diễn ra.', en: 'No ongoing classes yet.' },
        { vi: 'Chưa tìm thấy gia sư phù hợp với tiêu chí lọc.', en: 'No tutors found matching the criteria.' },
        { vi: 'Chưa có đánh giá nào trên hệ thống.', en: 'No reviews found in the system.' },
        { vi: 'Chưa có đánh giá', en: 'No reviews yet' },
        { vi: 'Chưa có lớp học nào.', en: 'No classes found.' },
        { vi: 'Bạn chưa có lớp học nào.', en: 'You have no classes yet.' },
        { vi: 'Bạn chưa gửi đơn ứng tuyển cho lớp nào.', en: 'You have not applied to any classes yet.' },
        { vi: 'Bạn chưa gửi yêu cầu học trực tiếp nào tới gia sư.', en: 'You have not sent any study requests to tutors.' },
        { vi: 'Bạn chưa có yêu cầu học nào', en: 'You have no study requests' },
        { vi: 'Chưa có yêu cầu học nào.', en: 'No study requests.' },
        { vi: 'Bạn chưa đăng yêu cầu tìm gia sư nào.', en: 'You have not posted any tutor requests yet.' },
        { vi: 'Đăng tin ngay bây giờ', en: 'Post a request now' },
        { vi: 'Đăng tin mới', en: 'Post New' },

        // Forms & Modals
        { vi: 'Tên đăng nhập', en: 'Username' },
        { vi: 'Mật khẩu', en: 'Password' },
        { vi: 'Xác nhận mật khẩu', en: 'Confirm Password' },
        { vi: 'Họ và tên', en: 'Full Name' },
        { vi: 'Số điện thoại', en: 'Phone Number' },
        { vi: 'Email liên hệ', en: 'Contact Email' },
        { vi: 'Địa chỉ', en: 'Address' },
        { vi: 'Giới thiệu ngắn (Bio)', en: 'Short Bio' },
        { vi: 'Ảnh đại diện', en: 'Profile Avatar' },
        { vi: 'Đổi ảnh đại diện', en: 'Change Avatar' },
        { vi: 'Lưu Thông Tin Cá Nhân', en: 'Save Profile Info' },
        { vi: 'Cập nhật ảnh đại diện', en: 'Update Profile Picture' },
        { vi: 'Thu phóng ảnh', en: 'Zoom' },
        { vi: 'Lưu ảnh đại diện', en: 'Save Avatar' },
        { vi: 'Hủy', en: 'Cancel' },
        { vi: 'Hủy bỏ', en: 'Cancel' },
        { vi: 'Đóng', en: 'Close' },
        { vi: 'Xác nhận', en: 'Confirm' },
        { vi: 'Xóa', en: 'Delete' },
        { vi: 'Sửa tin', en: 'Edit Post' },
        { vi: 'Đóng bài', en: 'Close Post' },
        { vi: 'Lưu bài đăng', en: 'Save Post' },
        { vi: 'Quay lại', en: 'Go Back' },
        { vi: 'Gửi Đánh Giá Ngay', en: 'Submit Review Now' },
        { vi: 'Mức độ hài lòng của bạn', en: 'Your Satisfaction Level' },
        { vi: 'Nhận xét chi tiết', en: 'Detailed Comments' },
        { vi: 'Tiêu đề bài đăng', en: 'Request Title' },
        { vi: 'Thời gian rảnh / Lịch học', en: 'Available Schedule / Timetable' },
        { vi: 'Mô tả chi tiết & Yêu cầu gia sư', en: 'Detailed Description & Requirements' },
        { vi: 'Môn học cần học', en: 'Subject to Learn' },
        { vi: 'Mức ngân sách / thù lao', en: 'Proposed Budget / Rate' },
        { vi: 'Đơn vị ngân sách', en: 'Budget Unit' },
        { vi: 'Hình thức học', en: 'Study Mode' },
        { vi: 'Số buổi / tuần', en: 'Sessions / week' },
        { vi: 'Thời gian có thể học', en: 'Available Study Schedule' },
        { vi: 'Địa chỉ học', en: 'Study Location Address' },
        { vi: 'Chọn Tỉnh / Thành phố', en: 'Select Province / City' },
        { vi: '-- Chọn Tỉnh / Thành phố --', en: '-- Select Province / City --' },
        { vi: 'Chọn Quận / Huyện', en: 'Select District' },
        { vi: '-- Chọn Quận / Huyện --', en: '-- Select District --' },
        { vi: 'Địa chỉ cụ thể (Số nhà, đường...)', en: 'Specific Address (House No, Street...)' },
        { vi: 'Địa chỉ đã chọn:', en: 'Selected Address:' },
        { vi: 'Chưa xác định', en: 'Not Specified' },
        { vi: 'Ghi chú, mục tiêu học tập & yêu cầu với gia sư', en: 'Notes, learning goals & requirements for tutor' },
        { vi: 'Xác Nhận Gửi Yêu Cầu', en: 'Confirm & Send Study Request' },
        { vi: 'Đồng ý nhận dạy', en: 'Accept Teaching Request' },
        { vi: 'Đánh dấu hoàn thành', en: 'Mark as Completed' },
        { vi: 'Hủy lớp', en: 'Cancel Class' },
        { vi: 'Viết Đánh Giá Gia Sư', en: 'Write Tutor Review' },
        { vi: 'Học Sinh / Phụ Huynh', en: 'Student / Parent' },
        { vi: 'Gia Sư Giảng Dạy', en: 'Assigned Tutor' },
        { vi: 'Địa chỉ liên hệ:', en: 'Contact Address:' },
        { vi: 'Địa điểm học của lớp:', en: 'Class Location:' },
        { vi: 'Mục tiêu & Yêu cầu học tập:', en: 'Learning Goals & Requirements:' },
        { vi: 'Giới thiệu gia sư:', en: 'Tutor Introduction:' },
        { vi: 'Bằng cấp / Chứng chỉ:', en: 'Degrees / Certificates:' },
        { vi: 'Xem tệp đính kèm', en: 'View Attached File' },
        { vi: 'Link minh chứng', en: 'Proof Link' },
        { vi: 'Xem hồ sơ đầy đủ của gia sư', en: 'View full tutor profile' },
        { vi: 'Thông Tin & Thỏa Thuận Lớp Học', en: 'Class Agreement & Information' },
        { vi: 'Số buổi học:', en: 'Sessions:' },
        { vi: 'Hình thức dạy:', en: 'Teaching Mode:' },
        { vi: 'Thời gian học / Khung giờ:', en: 'Class Timetable / Slots:' },
        { vi: 'Địa điểm diễn ra lớp học:', en: 'Class Location:' },
        { vi: 'Đánh Giá Từ Học Sinh', en: 'Review From Student' },
        { vi: 'Đánh giá từ HS', en: 'Student Review' },
        { vi: 'Quản lý lớp', en: 'Manage Class' },
        { vi: 'Chờ học sinh duyệt', en: 'Pending Student Approval' },
        { vi: 'Học sinh đã duyệt', en: 'Approved by Student' },
        { vi: 'Không được chọn', en: 'Not Selected' },
        { vi: 'Xem lớp đang cần gia sư', en: 'View Classes Needed' },
        { vi: 'Xem yêu cầu học', en: 'View Study Requests' },
        { vi: 'Tìm lớp đang cần gia sư', en: 'Find Classes Needing Tutors' },
        { vi: 'Đăng nhập để ứng tuyển', en: 'Log In to Apply' },
        { vi: 'Nội Dung Yêu Cầu Chi Tiết', en: 'Detailed Request Description' },
        { vi: 'Danh Sách Gia Sư Muốn Nhận Lớp', en: 'Tutors Applied For This Class' },

        // Days & Timetable
        { vi: 'Sáng', en: 'Morning' },
        { vi: 'Chiều', en: 'Afternoon' },
        { vi: 'Tối', en: 'Evening' },
        { vi: 'Thứ 2', en: 'Mon' },
        { vi: 'Thứ 3', en: 'Tue' },
        { vi: 'Thứ 4', en: 'Wed' },
        { vi: 'Thứ 5', en: 'Thu' },
        { vi: 'Thứ 6', en: 'Fri' },
        { vi: 'Thứ 7', en: 'Sat' },
        { vi: 'Chủ Nhật', en: 'Sun' },
        { vi: 'Chủ nhật', en: 'Sunday' },
        { vi: 'Các ngày trong tuần (Thứ 2 - Thứ 6)', en: 'Weekdays (Mon - Fri)' },
        { vi: 'Cuối tuần', en: 'Weekend' },
        { vi: '⚡ Tối 2, 4, 6', en: '⚡ Mon, Wed, Fri (Eve)' },
        { vi: '⚡ Tối 3, 5, 7', en: '⚡ Tue, Thu, Sat (Eve)' },
        { vi: '⚡ Cuối tuần (T7, CN)', en: '⚡ Weekend (Sat, Sun)' },
        { vi: '⚡ Tất cả các tối', en: '⚡ All Evenings' },
        { vi: '🔄 Xóa chọn', en: '🔄 Clear' },
        { vi: 'Chưa chọn buổi nào', en: 'No sessions selected' },

        // Tutor detail tabs & sections
        { vi: 'THÔNG TIN GIA SƯ', en: 'TUTOR INFORMATION' },
        { vi: 'Thông tin cơ bản', en: 'Basic Information' },
        { vi: 'Năm sinh:', en: 'Birth Year:' },
        { vi: 'Giới tính:', en: 'Gender:' },
        { vi: 'Quê quán:', en: 'Hometown:' },
        { vi: 'Giọng nói:', en: 'Voice / Accent:' },
        { vi: 'Học vấn:', en: 'Academic Level:' },
        { vi: 'Kinh nghiệm gia sư, giảng dạy', en: 'Teaching & Tutoring Experience' },
        { vi: 'Thành tích trong học tập và dạy học', en: 'Academic & Teaching Achievements' },
        { vi: 'MÔN HỌC & LỚP DẠY', en: 'SUBJECTS & CLASSES' },
        { vi: 'Môn học nhận dạy', en: 'Subjects Offered' },
        { vi: 'Lớp dạy / Đối tượng', en: 'Target Grades' },
        { vi: 'LỊCH DẠY CÓ THỂ ĐI DẠY', en: 'AVAILABLE TEACHING SCHEDULE' },
        { vi: 'Buổi / Thứ', en: 'Session / Day' },
        { vi: 'ĐÁNH GIÁ TỪ HỌC SINH & PHỤ HUYNH', en: 'REVIEWS FROM STUDENTS & PARENTS' },

        // Select options & subjects
        { vi: 'Toán học', en: 'Mathematics' },
        { vi: 'Vật lý', en: 'Physics' },
        { vi: 'Hóa học', en: 'Chemistry' },
        { vi: 'Tiếng Anh', en: 'English' },
        { vi: 'Ngữ văn', en: 'Literature' },
        { vi: 'Sinh học', en: 'Biology' },
        { vi: 'Lịch sử', en: 'History' },
        { vi: 'Địa lý', en: 'Geography' },
        { vi: 'Tin học', en: 'Informatics / IT' },
        { vi: 'Tiếng Trung', en: 'Chinese' },
        { vi: 'Tiếng Nhật', en: 'Japanese' },
        { vi: 'Tiếng Hàn', en: 'Korean' },
        { vi: 'Tiếng Pháp', en: 'French' },
        { vi: 'Cờ vua', en: 'Chess' },
        { vi: 'Bơi lội', en: 'Swimming' },
        { vi: 'Võ thuật', en: 'Martial Arts' },
        { vi: 'Cầu lông', en: 'Badminton' },
        { vi: 'Theo buổi', en: 'Per session' },
        { vi: 'Theo tháng', en: 'Per month' },
        { vi: 'Theo khóa', en: 'Per course' },
        { vi: 'Nam', en: 'Male' },
        { vi: 'Nữ', en: 'Female' },
        { vi: 'Khác', en: 'Other' },
        { vi: 'Sinh viên', en: 'University Student' },
        { vi: 'Giáo viên', en: 'Teacher / Lecturer' },
        { vi: 'Đã tốt nghiệp', en: 'Graduated / Working' },
        { vi: 'Năm 1', en: '1st Year' },
        { vi: 'Năm 2', en: '2nd Year' },
        { vi: 'Năm 3', en: '3rd Year' },
        { vi: 'Năm 4', en: '4th Year' },
        { vi: 'Năm cuối', en: 'Final Year' },
        { vi: 'Cử nhân', en: "Bachelor's" },
        { vi: 'Thạc sĩ', en: "Master's" },
        { vi: 'Tiến sĩ', en: 'PhD / Doctorate' },
        { vi: 'Miền Bắc', en: 'Northern Accent' },
        { vi: 'Miền Trung', en: 'Central Accent' },
        { vi: 'Miền Nam', en: 'Southern Accent' },
        { vi: '1 buổi/tuần', en: '1 session/week' },
        { vi: '2 buổi/tuần', en: '2 sessions/week' },
        { vi: '3 buổi/tuần', en: '3 sessions/week' },
        { vi: '4 buổi/tuần', en: '4 sessions/week' },
        { vi: '5 buổi/tuần', en: '5 sessions/week' },
        { vi: 'Hàng ngày', en: 'Daily' },

        // AI Assistant
        { vi: 'Hỏi Trợ Lý', en: 'Ask AI' },
        { vi: 'Trợ Lý AI TutorLink', en: 'TutorLink AI Assistant' },
        { vi: 'Trợ lý ảo sẵn sàng hỗ trợ 24/7', en: 'Virtual assistant ready 24/7' },
        { vi: 'Chọn nhanh câu hỏi bạn quan tâm:', en: 'Quick questions you might ask:' },
        { vi: '📚 Tìm lớp gia sư?', en: '📚 Find tutoring jobs?' },
        { vi: '🔍 Tìm gia sư giỏi?', en: '🔍 Find top tutors?' },
        { vi: '📝 Đăng tin tìm gia sư?', en: '📝 Post tutor request?' },
        { vi: '💰 Mức học phí?', en: '💰 Tutoring rates?' },
        { vi: '⚡ Quy trình ghép lớp?', en: '⚡ Matching process?' },
        { vi: '📞 Hotline hỗ trợ?', en: '📞 Support hotline?' }
    ];

    // Tạo bản đồ tra cứu nhanh theo văn bản chuẩn hóa
    const PHRASE_LOOKUP_VI_TO_EN = new Map();
    const PHRASE_LOOKUP_EN_TO_VI = new Map();

    PHRASE_MAP.forEach(item => {
        const viClean = item.vi.trim();
        const enClean = item.en.trim();
        if (viClean && enClean) {
            PHRASE_LOOKUP_VI_TO_EN.set(viClean, enClean);
            PHRASE_LOOKUP_EN_TO_VI.set(enClean, viClean);
        }
    });

    // 3. BỘ ĐIỀU KHIỂN CHUYỂN ĐỔI NGÔN NGỮ (Language Controller)
    const TutorLinkI18n = {
        currentLang: 'vi',

        // Lấy ngôn ngữ hiện tại
        getLanguage: function() {
            try {
                return localStorage.getItem('tutorlink_lang') || 'vi';
            } catch(e) {
                return this.currentLang || 'vi';
            }
        },

        // Đặt ngôn ngữ (chuyển đổi giữa 'vi' và 'en')
        setLanguage: function(lang) {
            lang = (lang === 'en') ? 'en' : 'vi';
            this.currentLang = lang;

            document.documentElement.setAttribute('lang', lang);
            document.documentElement.setAttribute('data-lang', lang);

            try {
                localStorage.setItem('tutorlink_lang', lang);
            } catch(e) {}

            this.applyLanguage(lang);
            this.syncLanguageUI(lang);
        },

        // Đồng bộ trạng thái active của các nút chọn cờ trên Header / Dropdown
        syncLanguageUI: function(lang) {
            const currentLang = lang || this.getLanguage();
            const viBtns = document.querySelectorAll('#btn-lang-vi, .guest-btn-lang-vi, [data-lang-btn="vi"]');
            const enBtns = document.querySelectorAll('#btn-lang-en, .guest-btn-lang-en, [data-lang-btn="en"]');

            viBtns.forEach(el => {
                if (currentLang === 'vi') el.classList.add('active');
                else el.classList.remove('active');
            });
            enBtns.forEach(el => {
                if (currentLang === 'en') el.classList.add('active');
                else el.classList.remove('active');
            });
        },

        // Tra cứu dịch bằng khóa
        t: function(key, defaultText) {
            const lang = this.getLanguage();
            if (TRANSLATIONS[key] && TRANSLATIONS[key][lang]) {
                return TRANSLATIONS[key][lang];
            }
            return defaultText || key;
        },

        // Áp dụng dịch lên toàn bộ DOM
        applyLanguage: function(lang) {
            lang = (lang === 'en') ? 'en' : 'vi';
            this.currentLang = lang;

            // 1. Áp dụng cho các phần tử có data-i18n
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (TRANSLATIONS[key] && TRANSLATIONS[key][lang]) {
                    el.textContent = TRANSLATIONS[key][lang];
                }
            });

            // 2. Áp dụng cho data-i18n-title
            document.querySelectorAll('[data-i18n-title]').forEach(el => {
                const key = el.getAttribute('data-i18n-title');
                if (TRANSLATIONS[key] && TRANSLATIONS[key][lang]) {
                    const val = TRANSLATIONS[key][lang];
                    el.setAttribute('title', val);
                    el.setAttribute('aria-label', val);
                }
            });

            // 3. Áp dụng cho data-i18n-placeholder
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
                const key = el.getAttribute('data-i18n-placeholder');
                if (TRANSLATIONS[key] && TRANSLATIONS[key][lang]) {
                    el.setAttribute('placeholder', TRANSLATIONS[key][lang]);
                }
            });

            // 4. Dịch các thuộc tính placeholder thông dụng trên các input & textarea
            this.translatePlaceholders(lang);

            // 5. Dịch các options trong select và optgroup
            this.translateSelectOptions(lang);

            // 6. Quét và dịch thông minh các nút văn bản (Text Nodes) trên giao diện
            this.translateDOMTextNodes(lang);

            // 7. Cập nhật cụ thể cho widget Trợ lý AI nếu đang hiển thị
            this.translateAssistantWidget(lang);
        },

        // Dịch các placeholder input
        translatePlaceholders: function(lang) {
            const inputs = document.querySelectorAll('input[placeholder], textarea[placeholder]');
            inputs.forEach(input => {
                if (!input._origPlaceholder) {
                    input._origPlaceholder = input.getAttribute('placeholder');
                }
                const original = input._origPlaceholder.trim();
                if (lang === 'en') {
                    if (PHRASE_LOOKUP_VI_TO_EN.has(original)) {
                        input.setAttribute('placeholder', PHRASE_LOOKUP_VI_TO_EN.get(original));
                    }
                } else {
                    input.setAttribute('placeholder', input._origPlaceholder);
                }
            });
        },

        // Dịch các select options
        translateSelectOptions: function(lang) {
            const options = document.querySelectorAll('select option');
            options.forEach(opt => {
                if (typeof opt._origText === 'undefined') {
                    opt._origText = opt.textContent;
                }
                if (lang === 'vi') {
                    opt.textContent = opt._origText;
                } else {
                    const trimmed = opt._origText.trim();
                    if (PHRASE_LOOKUP_VI_TO_EN.has(trimmed)) {
                        opt.textContent = PHRASE_LOOKUP_VI_TO_EN.get(trimmed);
                    }
                }
            });

            const optgroups = document.querySelectorAll('select optgroup');
            optgroups.forEach(og => {
                if (typeof og._origLabel === 'undefined') {
                    og._origLabel = og.getAttribute('label') || '';
                }
                if (lang === 'vi') {
                    og.setAttribute('label', og._origLabel);
                } else {
                    const trimmed = (og._origLabel || '').trim();
                    if (PHRASE_LOOKUP_VI_TO_EN.has(trimmed)) {
                        og.setAttribute('label', PHRASE_LOOKUP_VI_TO_EN.get(trimmed));
                    }
                }
            });
        },

        // Quét và dịch văn bản trên các Text Node mà không làm hỏng cấu trúc HTML
        translateDOMTextNodes: function(lang) {
            // Không quét các thẻ script, style, textarea, input, code, pre
            const ignoreTags = new Set(['SCRIPT', 'STYLE', 'TEXTAREA', 'INPUT', 'SELECT', 'CODE', 'PRE', 'NOSCRIPT']);
            const root = document.body;
            if (!root) return;

            const walker = document.createTreeWalker(
                root,
                NodeFilter.SHOW_TEXT,
                {
                    acceptNode: function(node) {
                        const parent = node.parentElement;
                        if (!parent) return NodeFilter.FILTER_REJECT;
                        if (ignoreTags.has(parent.tagName)) return NodeFilter.FILTER_REJECT;
                        if (parent.closest('[data-no-i18n]') || parent.isContentEditable) return NodeFilter.FILTER_REJECT;
                        if (parent.hasAttribute('data-i18n')) return NodeFilter.FILTER_REJECT; // Đã dịch qua key
                        
                        const text = node.nodeValue.trim();
                        if (!text || text.length < 2) return NodeFilter.FILTER_SKIP;
                        return NodeFilter.FILTER_ACCEPT;
                    }
                },
                false
            );

            let node;
            const nodesToTranslate = [];
            while ((node = walker.nextNode())) {
                nodesToTranslate.push(node);
            }

            nodesToTranslate.forEach(textNode => {
                // Lưu trữ text gốc tiếng Việt ban đầu
                if (typeof textNode._originalText === 'undefined') {
                    textNode._originalText = textNode.nodeValue;
                }

                if (lang === 'vi') {
                    // Phục hồi nguyên bản tiếng Việt 100% không mất mát
                    if (textNode._originalText !== textNode.nodeValue) {
                        textNode.nodeValue = textNode._originalText;
                    }
                } else if (lang === 'en') {
                    const raw = textNode._originalText;
                    const trimmed = raw.trim();

                    if (PHRASE_LOOKUP_VI_TO_EN.has(trimmed)) {
                        const translated = PHRASE_LOOKUP_VI_TO_EN.get(trimmed);
                        // Giữ nguyên khoảng trắng đầu/cuối của chuỗi
                        const leadingSpaces = raw.match(/^\s*/)[0];
                        const trailingSpaces = raw.match(/\s*$/)[0];
                        textNode.nodeValue = leadingSpaces + translated + trailingSpaces;
                    } else {
                        // Xử lý các mẫu câu động bằng Regex thông minh
                        let modified = raw;
                        let changed = false;

                        // Tiền tố & trạng thái
                        if (modified.includes('Bắt đầu ngày ')) {
                            modified = modified.replace(/Bắt đầu ngày /g, 'Started on ');
                            changed = true;
                        }
                        if (modified.includes('Đăng ngày ')) {
                            modified = modified.replace(/Đăng ngày /g, 'Posted on ');
                            changed = true;
                        }
                        if (modified.includes('Đánh giá ngày ')) {
                            modified = modified.replace(/Đánh giá ngày /g, 'Reviewed on ');
                            changed = true;
                        }
                        if (modified.includes('Bởi ')) {
                            modified = modified.replace(/Bởi /g, 'By ');
                            changed = true;
                        }
                        if (modified.includes('Đã chọn: ')) {
                            modified = modified.replace(/Đã chọn: /g, 'Selected: ');
                            changed = true;
                        }
                        if (modified.includes('Lớp: ')) {
                            modified = modified.replace(/Lớp: /g, 'Class: ');
                            changed = true;
                        }
                        if (modified.includes('Môn ')) {
                            modified = modified.replace(/Môn /g, 'Subject ');
                            changed = true;
                        }
                        if (modified.includes('Xin chào, thầy/cô ')) {
                            modified = modified.replace(/Xin chào, thầy\/cô /g, 'Hello, Tutor ');
                            changed = true;
                        } else if (modified.includes('Xin chào, ')) {
                            modified = modified.replace(/Xin chào, /g, 'Hello, ');
                            changed = true;
                        }

                        // Đơn vị tiền tệ & số lượng
                        if (modified.includes(' đ/buổi')) {
                            modified = modified.replace(/ đ\/buổi/g, ' VND/session');
                            changed = true;
                        }
                        if (modified.includes(' đ/giờ')) {
                            modified = modified.replace(/ đ\/giờ/g, ' VND/hour');
                            changed = true;
                        }
                        if (modified.includes(' đ/h')) {
                            modified = modified.replace(/ đ\/h/g, ' VND/hr');
                            changed = true;
                        }
                        if (modified.includes(' đ/tháng')) {
                            modified = modified.replace(/ đ\/tháng/g, ' VND/month');
                            changed = true;
                        }
                        if (modified.includes(' đ/khóa')) {
                            modified = modified.replace(/ đ\/khóa/g, ' VND/course');
                            changed = true;
                        }
                        if (modified.includes(' đ')) {
                            modified = modified.replace(/ đ/g, ' VND');
                            changed = true;
                        }
                        if (modified.includes(' lớp đã hoàn thành')) {
                            modified = modified.replace(/ lớp đã hoàn thành/g, ' completed classes');
                            changed = true;
                        }
                        if (modified.includes(' đánh giá')) {
                            modified = modified.replace(/ đánh giá/g, ' reviews');
                            changed = true;
                        }
                        if (modified.includes(' gia sư')) {
                            modified = modified.replace(/ gia sư/g, ' tutors');
                            changed = true;
                        }
                        if (modified.includes(' bài đăng')) {
                            modified = modified.replace(/ bài đăng/g, ' posts');
                            changed = true;
                        }
                        if (modified.includes(' ứng viên')) {
                            modified = modified.replace(/ ứng viên/g, ' candidates');
                            changed = true;
                        }
                        if (modified.includes(' gia sư chờ bạn duyệt')) {
                            modified = modified.replace(/ gia sư chờ bạn duyệt/g, ' tutors awaiting your approval');
                            changed = true;
                        }
                        if (modified.includes(' buổi/tuần')) {
                            modified = modified.replace(/ buổi\/tuần/g, ' sessions/week');
                            changed = true;
                        }

                        if (changed) {
                            textNode.nodeValue = modified;
                        }
                    }
                }
            });
        },

        // Dịch widget Trợ lý AI chuyên biệt
        translateAssistantWidget: function(lang) {
            const widget = document.getElementById('assistant-modal');
            if (!widget) return;

            const titleEl = document.getElementById('assistant-header-title');
            if (titleEl) {
                titleEl.textContent = (lang === 'en') ? 'TutorLink AI Assistant' : 'Trợ Lý AI TutorLink';
            }

            const inputEl = document.getElementById('assistant-input');
            if (inputEl) {
                inputEl.setAttribute('placeholder', (lang === 'en') ? 'Type a question for AI...' : 'Nhập câu hỏi cho AI...');
            }

            const roundTag = document.querySelector('.assistant-round-tag span');
            if (roundTag) {
                roundTag.textContent = (lang === 'en') ? 'Ask AI' : 'Hỏi Trợ Lý';
            }

            const toggleBtn = document.getElementById('assistant-toggle-btn');
            if (toggleBtn) {
                toggleBtn.setAttribute('title', (lang === 'en') ? 'Ask TutorLink AI Assistant' : 'Hỏi Trợ Lý AI TutorLink (Nhấp để trò chuyện / Kéo để di chuyển)');
            }
        },

        // Khởi tạo
        init: function() {
            const savedLang = this.getLanguage();
            this.setLanguage(savedLang);

            // Thiết lập MutationObserver để tự động dịch các modal hay nội dung thêm động vào trang
            let debounceTimer = null;
            const observer = new MutationObserver(mutations => {
                const currentLang = this.getLanguage();
                if (currentLang !== 'en') return; // Tiếng Việt là mặc định

                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => {
                    this.applyLanguage(currentLang);
                }, 100);
            });

            if (document.body) {
                observer.observe(document.body, {
                    childList: true,
                    subtree: true
                });
            }
        }
    };

    // Export ra Window toàn cục để các script khác sử dụng trực tiếp
    window.TUTORLINK_TRANSLATIONS = TRANSLATIONS;
    window.TutorLinkI18n = TutorLinkI18n;
    window.setLanguage = function(lang) {
        TutorLinkI18n.setLanguage(lang);
    };
    window.getLanguage = function() {
        return TutorLinkI18n.getLanguage();
    };
    window.applyLanguage = function(lang) {
        TutorLinkI18n.applyLanguage(lang);
    };
    window.syncLanguageUI = function(lang) {
        TutorLinkI18n.syncLanguageUI(lang);
    };
    window.t = function(key, defaultText) {
        return TutorLinkI18n.t(key, defaultText);
    };

    // Tự động kích hoạt khi DOM sẵn sàng
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            TutorLinkI18n.init();
        });
    } else {
        TutorLinkI18n.init();
    }

})(window, document);
