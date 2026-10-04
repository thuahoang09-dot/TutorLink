# Danh sách 63 tỉnh thành Việt Nam và các thành phố lớn

POPULAR_CITIES = [
    'Hà Nội',
    'TP. Hồ Chí Minh',
    'Đà Nẵng',
    'Hải Phòng',
    'Cần Thơ',
]

VIETNAM_PROVINCES = [
    'An Giang',
    'Bà Rịa - Vũng Tàu',
    'Bắc Giang',
    'Bắc Kạn',
    'Bạc Liêu',
    'Bắc Ninh',
    'Bến Tre',
    'Bình Định',
    'Bình Dương',
    'Bình Phước',
    'Bình Thuận',
    'Cà Mau',
    'Cần Thơ',
    'Cao Bằng',
    'Đà Nẵng',
    'Đắk Lắk',
    'Đắk Nông',
    'Điện Biên',
    'Đồng Nai',
    'Đồng Tháp',
    'Gia Lai',
    'Hà Giang',
    'Hà Nam',
    'Hà Nội',
    'Hà Tĩnh',
    'Hải Dương',
    'Hải Phòng',
    'Hậu Giang',
    'Hòa Bình',
    'Hưng Yên',
    'Khánh Hòa',
    'Kiên Giang',
    'Kon Tum',
    'Lai Châu',
    'Lâm Đồng',
    'Lạng Sơn',
    'Lào Cai',
    'Long An',
    'Nam Định',
    'Nghệ An',
    'Ninh Bình',
    'Ninh Thuận',
    'Phú Thọ',
    'Phú Yên',
    'Quảng Bình',
    'Quảng Nam',
    'Quảng Ngãi',
    'Quảng Ninh',
    'Quảng Trị',
    'Sóc Trăng',
    'Sơn La',
    'Tây Ninh',
    'Thái Bình',
    'Thái Nguyên',
    'Thanh Hóa',
    'Thừa Thiên Huế',
    'Tiền Giang',
    'TP. Hồ Chí Minh',
    'Trà Vinh',
    'Tuyên Quang',
    'Vĩnh Long',
    'Vĩnh Phúc',
    'Yên Bái',
]

VIETNAM_DISTRICTS = {
    'Hà Nội': [
        'Phường Dịch Vọng', 'Phường Dịch Vọng Hậu', 'Phường Nghĩa Tân', 'Phường Mai Dịch', 'Phường Yên Hòa', 'Phường Trung Hòa',
        'Phường Hàng Bài', 'Phường Hàng Bạc', 'Phường Hàng Đào', 'Phường Tràng Tiền', 'Phường Cửa Nam',
        'Phường Bách Khoa', 'Phường Đồng Tâm', 'Phường Bạch Mai', 'Phường Minh Khai', 'Phường Trương Định',
        'Phường Kim Liên', 'Phường Ô Chợ Dừa', 'Phường Láng Thượng', 'Phường Láng Hạ', 'Phường Văn Miếu',
        'Phường Mỹ Đình 1', 'Phường Mỹ Đình 2', 'Phường Mễ Trì', 'Phường Phú Đô', 'Phường Trung Văn',
        'Phường Khương Trung', 'Phường Khương Mai', 'Phường Nhân Chính', 'Phường Thanh Xuân Bắc',
        'Phường Hoàng Liệt', 'Phường Định Công', 'Phường Giáp Bát', 'Phường Tân Mai',
        'Phường Mộ Lao', 'Phường Văn Quán', 'Phường Hà Cầu', 'Phường Quang Trung', 'Phường Yết Kiêu',
        'Phường Ngọc Hà', 'Phường Đội Cấn', 'Phường Liễu Giai', 'Phường Kim Mã', 'Phường Giảng Võ',
        'Phường Bồ Đề', 'Phường Gia Thụy', 'Phường Ngọc Lâm', 'Phường Thạch Bàn', 'Phường Long Biên',
        'Xã Đông Anh', 'Xã Cổ Loa', 'Xã Bát Tràng', 'Xã An Khánh', 'Xã Đan Phượng', 'Xã Hoài Đức',
        'Xã Quốc Oai', 'Xã Thạch Thất', 'Xã Chương Mỹ', 'Xã Thanh Oai', 'Xã Thường Tín',
        'Cầu Giấy', 'Đống Đa', 'Ba Đình', 'Hoàn Kiếm', 'Hai Bà Trưng', 'Thanh Xuân', 'Hà Đông', 'Nam Từ Liêm', 'Bắc Từ Liêm'
    ],
    'TP. Hồ Chí Minh': [
        'Phường Bến Nghé', 'Phường Bến Thành', 'Phường Đa Kao', 'Phường Tân Định', 'Phường Cầu Ông Lãnh',
        'Phường Võ Thị Sáu', 'Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5',
        'Phường Thảo Điền', 'Phường An Phú', 'Phường Thủ Thiêm', 'Phường Linh Trung', 'Phường Linh Chiểu', 'Phường Hiệp Bình Chánh', 'Phường Hiệp Phú', 'Phường Phước Long B',
        'Phường Tân Phong', 'Phường Tân Phú', 'Phường Phú Thuận', 'Phường Tân Quy',
        'Phường 25 (Bình Thạnh)', 'Phường 14 (Quận 10)', 'Phường 2 (Tân Bình)', 'Phường 10 (Gò Vấp)', 'Phường 9 (Phú Nhuận)', 'Phường 11 (Quận 5)',
        'Phường Bình Hưng Hòa', 'Phường Bình Trị Đông', 'Phường Tân Sơn Nhì', 'Phường Tân Thới Nhất',
        'Xã Bình Hưng', 'Xã Phong Phú', 'Xã Tân Kiên', 'Xã Hóc Môn', 'Xã Củ Chi', 'Xã Nhà Bè', 'Xã Cần Giờ',
        'Quận 1', 'Quận 3', 'Quận 5', 'Quận 7', 'Quận 10', 'Bình Thạnh', 'Tân Bình', 'Gò Vấp', 'Phú Nhuận', 'Tân Phú', 'Bình Tân', 'TP. Thủ Đức'
    ],
    'Hồ Chí Minh': [
        'Phường Bến Nghé', 'Phường Bến Thành', 'Phường Đa Kao', 'Phường Tân Định', 'Phường Cầu Ông Lãnh',
        'Phường Võ Thị Sáu', 'Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5',
        'Phường Thảo Điền', 'Phường An Phú', 'Phường Thủ Thiêm', 'Phường Linh Trung', 'Phường Linh Chiểu', 'Phường Hiệp Bình Chánh', 'Phường Hiệp Phú', 'Phường Phước Long B',
        'Phường Tân Phong', 'Phường Tân Phú', 'Phường Phú Thuận', 'Phường Tân Quy',
        'Phường 25 (Bình Thạnh)', 'Phường 14 (Quận 10)', 'Phường 2 (Tân Bình)', 'Phường 10 (Gò Vấp)', 'Phường 9 (Phú Nhuận)', 'Phường 11 (Quận 5)',
        'Phường Bình Hưng Hòa', 'Phường Bình Trị Đông', 'Phường Tân Sơn Nhì', 'Phường Tân Thới Nhất',
        'Xã Bình Hưng', 'Xã Phong Phú', 'Xã Tân Kiên', 'Xã Hóc Môn', 'Xã Củ Chi', 'Xã Nhà Bè', 'Xã Cần Giờ',
        'Quận 1', 'Quận 3', 'Quận 5', 'Quận 7', 'Quận 10', 'Bình Thạnh', 'Tân Bình', 'Gò Vấp', 'Phú Nhuận', 'Tân Phú', 'Bình Tân', 'TP. Thủ Đức'
    ],
    'Đà Nẵng': [
        'Phường Hải Châu 1', 'Phường Hải Châu 2', 'Phường Thạch Thang', 'Phường Thanh Bình', 'Phường Thuận Phước',
        'Phường Thạc Gián', 'Phường Vĩnh Trung', 'Phường Tam Thuận', 'Phường An Khê',
        'Phường An Hải Bắc', 'Phường Phước Mỹ', 'Phường Nại Hiên Đông',
        'Phường Khuê Mỹ', 'Phường Mỹ An', 'Phường Hòa Hải',
        'Phường Hòa Minh', 'Phường Hòa Khánh Bắc', 'Phường Hòa Khánh Nam',
        'Phường Khuê Trung', 'Phường Hòa Thọ Đông', 'Xã Hòa Vang',
        'Hải Châu', 'Thanh Khê', 'Sơn Trà', 'Ngũ Hành Sơn', 'Liên Chiểu', 'Cẩm Lệ'
    ],
    'Hải Phòng': [
        'Phường Hoàng Văn Thụ', 'Phường Minh Khai', 'Phường Phan Bội Châu',
        'Phường Cầu Đất', 'Phường Lạch Tray', 'Phường Đằng Giang',
        'Phường Lam Sơn', 'Phường An Dương', 'Phường Niệm Nghĩa',
        'Phường Đằng Hải', 'Phường Nam Hải', 'Phường Vạn Sơn',
        'Xã Thủy Nguyên', 'Xã An Lão', 'Xã Kiến Thụy', 'Xã Tiên Lãng', 'Xã Vĩnh Bảo', 'Xã Cát Hải',
        'Hồng Bàng', 'Ngô Quyền', 'Lê Chân', 'Hải An', 'Kiến An'
    ],
    'Cần Thơ': [
        'Phường An Cư', 'Phường An Hòa', 'Phường Cái Khế', 'Phường Tân An', 'Phường Xuân Khánh',
        'Phường An Thới', 'Phường Bình Thủy', 'Phường Trà Nóc',
        'Phường Hưng Phú', 'Phường Hưng Thạnh', 'Phường Tân Phú',
        'Phường Thốt Nốt', 'Phường Trung Kiên',
        'Xã Phong Điền', 'Xã Thới Lai', 'Xã Cờ Đỏ', 'Xã Vĩnh Thạnh',
        'Ninh Kiều', 'Bình Thủy', 'Cái Răng', 'Ô Môn'
    ],
    'Bình Dương': [
        'Thủ Dầu Một', 'Dĩ An', 'Thuận An', 'Bến Cát', 'Tân Uyên',
        'Bắc Tân Uyên', 'Bàu Bàng', 'Dầu Tiếng', 'Phú Giáo'
    ],
    'Đồng Nai': [
        'Biên Hòa', 'Long Khánh', 'Cẩm Mỹ', 'Định Quán', 'Long Thành',
        'Nhơn Trạch', 'Tân Phú', 'Thống Nhất', 'Trảng Bom', 'Vĩnh Cửu', 'Xuân Lộc'
    ],
    'Quảng Ninh': [
        'Hạ Long', 'Cẩm Phả', 'Uông Bí', 'Móng Cái', 'Quảng Yên',
        'Đông Triều', 'Vân Đồn', 'Tiên Yên', 'Đầm Hà', 'Hải Hà', 'Ba Chẽ',
        'Bình Liêu', 'Cô Tô'
    ],
    'Khánh Hòa': [
        'Nha Trang', 'Cam Ranh', 'Ninh Hòa', 'Vạn Ninh', 'Diên Khánh',
        'Khánh Vĩnh', 'Khánh Sơn', 'Cam Lâm', 'Trường Sa'
    ],
    'Bà Rịa - Vũng Tàu': [
        'Vũng Tàu', 'Bà Rịa', 'Phú Mỹ', 'Châu Đức', 'Côn Đảo', 'Đất Đỏ',
        'Long Điền', 'Xuyên Mộc'
    ],
    'Thừa Thiên Huế': [
        'TP. Huế', 'Hương Thủy', 'Hương Trà', 'A Lưới', 'Nam Đông',
        'Phong Điền', 'Phú Lộc', 'Phú Vang', 'Quảng Điền'
    ],
    'Nghệ An': [
        'TP. Vinh', 'Cửa Lò', 'Thái Hòa', 'Quỳnh Lưu', 'Diễn Châu',
        'Nghi Lộc', 'Yên Thành', 'Hưng Nguyên', 'Nghĩa Đàn', 'Quỳ Hợp',
        'Quỳ Châu', 'Quế Phong', 'Tân Kỳ', 'Đô Lương', 'Anh Sơn', 'Con Cuông',
        'Tương Dương', 'Kỳ Sơn', 'Nam Đàn', 'Thanh Chương'
    ],
    'Thanh Hóa': [
        'TP. Thanh Hóa', 'Sầm Sơn', 'Bỉm Sơn', 'Nghi Sơn', 'Đông Sơn',
        'Quảng Xương', 'Hoằng Hóa', 'Hậu Lộc', 'Hà Trung', 'Nga Sơn',
        'Thiệu Hóa', 'Triệu Sơn', 'Yên Định', 'Thọ Xuân', 'Vĩnh Lộc',
        'Thạch Thành', 'Cẩm Thủy', 'Ngọc Lặc', 'Lang Chánh', 'Bá Thước',
        'Quan Hóa', 'Quan Sơn', 'Mường Lát', 'Như Xuân', 'Như Thanh', 'Nông Cống'
    ],
    'Bắc Ninh': [
        'TP. Bắc Ninh', 'Từ Sơn', 'Yên Phong', 'Quế Võ', 'Tiên Du',
        'Thuận Thành', 'Gia Bình', 'Lương Tài'
    ],
    'Hải Dương': [
        'TP. Hải Dương', 'Chí Linh', 'Kinh Môn', 'Bình Giang', 'Cẩm Giàng',
        'Gia Lộc', 'Kim Thành', 'Nam Sách', 'Ninh Giang', 'Thanh Hà',
        'Thanh Miện', 'Tứ Kỳ'
    ],
    'Thái Nguyên': [
        'TP. Thái Nguyên', 'Sông Công', 'Phổ Yên', 'Đại Từ', 'Định Hóa',
        'Đồng Hỷ', 'Phú Bình', 'Phú Lương', 'Võ Nhai'
    ],
    'Nam Định': [
        'TP. Nam Định', 'Giao Thủy', 'Hải Hậu', 'Mỹ Lộc', 'Nam Trực',
        'Nghĩa Hưng', 'Trực Ninh', 'Vụ Bản', 'Xuân Trường', 'Ý Yên'
    ],
    'Thái Bình': [
        'TP. Thái Bình', 'Đông Hưng', 'Hưng Hà', 'Kiến Xương', 'Quỳnh Phụ',
        'Thái Thụy', 'Tiền Hải', 'Vũ Thư'
    ],
    'Lâm Đồng': [
        'Đà Lạt', 'Bảo Lộc', 'Bảo Lâm', 'Cát Tiên', 'Di Linh', 'Đạ Huoai',
        'Đạ Tẻh', 'Đam Rông', 'Đơn Dương', 'Đức Trọng', 'Lạc Dương'
    ],
    'Bình Định': [
        'Quy Nhơn', 'An Nhơn', 'Hoài Nhơn', 'An Lão', 'Hoài Ân', 'Phù Cát',
        'Phù Mỹ', 'Tuy Phước', 'Tây Sơn', 'Vân Canh', 'Vĩnh Thạnh'
    ],
    'Kiên Giang': [
        'Rạch Giá', 'Hà Tiên', 'Phú Quốc', 'An Biên', 'An Minh', 'Châu Thành',
        'Giang Thành', 'Giồng Riềng', 'Gò Quao', 'Hòn Đất', 'Kiên Hải',
        'Kiên Lương', 'Tân Hiệp', 'U Minh Thượng', 'Vĩnh Thuận'
    ],
    'An Giang': [
        'Long Xuyên', 'Châu Đốc', 'Tân Châu', 'An Phú', 'Châu Phú',
        'Châu Thành', 'Chợ Mới', 'Phú Tân', 'Thoại Sơn', 'Tịnh Biên', 'Tri Tôn'
    ],
    'Tiền Giang': [
        'Mỹ Tho', 'Gò Công', 'Cai Lậy', 'Cái Bè', 'Châu Thành', 'Chợ Gạo',
        'Gò Công Đông', 'Gò Công Tây', 'Tân Phước', 'Tân Phú Đông'
    ],
    'Vĩnh Long': [
        'TP. Vĩnh Long', 'Bình Minh', 'Bình Tân', 'Long Hồ', 'Mang Thít',
        'Tam Bình', 'Trà Ôn', 'Vũng Liêm'
    ],
    'Đồng Tháp': [
        'Cao Lãnh', 'Sa Đéc', 'Hồng Ngự', 'Châu Thành', 'Lai Vung', 'Lấp Vò',
        'Tam Nông', 'Tân Hồng', 'Thanh Bình', 'Tháp Mười'
    ],
    'Bắc Giang': [
        'TP. Bắc Giang', 'Việt Yên', 'Hiệp Hòa', 'Lạng Giang', 'Lục Nam',
        'Lục Ngạn', 'Sơn Động', 'Tân Yên', 'Yên Dũng', 'Yên Thế'
    ],
    'Phú Thọ': [
        'Việt Trì', 'Phú Thọ', 'Cẩm Khê', 'Đoan Hùng', 'Hạ Hòa', 'Lâm Thao',
        'Phù Ninh', 'Tam Nông', 'Tân Sơn', 'Thanh Ba', 'Thanh Sơn',
        'Thanh Thủy', 'Yên Lập'
    ],
    'Vĩnh Phúc': [
        'Vĩnh Yên', 'Phúc Yên', 'Bình Xuyên', 'Lập Thạch', 'Sông Lô',
        'Tam Dương', 'Tam Đảo', 'Vĩnh Tường', 'Yên Lạc'
    ],
    'Hưng Yên': [
        'TP. Hưng Yên', 'Mỹ Hào', 'Ân Thi', 'Khoái Châu', 'Kim Động',
        'Phù Cừ', 'Tiên Lữ', 'Văn Giang', 'Văn Lâm', 'Yên Mỹ'
    ],
    'Hà Nam': [
        'Phủ Lý', 'Duy Tiên', 'Bình Lục', 'Kim Bảng', 'Lý Nhân', 'Thanh Liêm'
    ],
    'Ninh Bình': [
        'TP. Ninh Bình', 'Tam Điệp', 'Gia Viễn', 'Hoa Lư', 'Kim Sơn',
        'Nho Quan', 'Yên Khánh', 'Yên Mô'
    ],
    'Hòa Bình': [
        'TP. Hòa Bình', 'Cao Phong', 'Đà Bắc', 'Kim Bôi', 'Lạc Sơn',
        'Lạc Thủy', 'Lương Sơn', 'Mai Châu', 'Tân Lạc', 'Yên Thủy'
    ],
    'Sơn La': [
        'TP. Sơn La', 'Bắc Yên', 'Mai Sơn', 'Mộc Châu', 'Mường La',
        'Phù Yên', 'Quỳnh Nhai', 'Sông Mã', 'Sốp Cộp', 'Thuận Châu',
        'Vân Hồ', 'Yên Châu'
    ],
    'Lào Cai': [
        'TP. Lào Cai', 'Sa Pa', 'Bát Xát', 'Bảo Thắng', 'Bảo Yên',
        'Bắc Hà', 'Mường Khương', 'Si Ma Cai', 'Văn Bàn'
    ],
    'Yên Bái': [
        'TP. Yên Bái', 'Nghĩa Lộ', 'Lục Yên', 'Mù Cang Chải', 'Trạm Tấu',
        'Trấn Yên', 'Văn Chấn', 'Văn Yên', 'Yên Bình'
    ],
    'Lạng Sơn': [
        'TP. Lạng Sơn', 'Bắc Sơn', 'Bình Gia', 'Cao Lộc', 'Chi Lăng',
        'Đình Lập', 'Hữu Lũng', 'Lộc Bình', 'Tràng Định', 'Văn Lãng', 'Văn Quan'
    ],
    'Tuyên Quang': [
        'TP. Tuyên Quang', 'Chiêm Hóa', 'Hàm Yên', 'Lâm Bình', 'Na Hang',
        'Sơn Dương', 'Yên Sơn'
    ],
    'Hà Giang': [
        'TP. Hà Giang', 'Bắc Mê', 'Bắc Quang', 'Đồng Văn', 'Hoàng Su Phì',
        'Mèo Vạc', 'Quản Bạ', 'Quang Bình', 'Vị Xuyên', 'Xín Mần', 'Yên Minh'
    ],
    'Cao Bằng': [
        'TP. Cao Bằng', 'Bảo Lạc', 'Bảo Lâm', 'Hạ Lang', 'Hà Quảng',
        'Hòa An', 'Nguyên Bình', 'Quảng Hòa', 'Thạch An', 'Trùng Khánh'
    ],
    'Bắc Kạn': [
        'TP. Bắc Kạn', 'Ba Bể', 'Bạch Thông', 'Chợ Đồn', 'Chợ Mới',
        'Na Rì', 'Ngân Sơn', 'Pác Nặm'
    ],
    'Điện Biên': [
        'TP. Điện Biên Phủ', 'Mường Lay', 'Điện Biên', 'Điện Biên Đông',
        'Mường Ảng', 'Mường Chà', 'Mường Nhé', 'Nậm Pồ', 'Tủa Chùa', 'Tuần Giáo'
    ],
    'Lai Châu': [
        'TP. Lai Châu', 'Mường Tè', 'Nậm Nhùn', 'Phong Thổ', 'Sìn Hồ',
        'Tam Đường', 'Tân Uyên', 'Than Uyên'
    ],
    'Quảng Bình': [
        'Đồng Hới', 'Ba Đồn', 'Bố Trạch', 'Lệ Thủy', 'Minh Hóa',
        'Quảng Ninh', 'Quảng Trạch', 'Tuyên Hóa'
    ],
    'Quảng Trị': [
        'Đông Hà', 'Quảng Trị', 'Cam Lộ', 'Cồn Cỏ', 'Đakrông',
        'Gio Linh', 'Hướng Hóa', 'Triệu Phong', 'Vĩnh Linh'
    ],
    'Quảng Nam': [
        'Tam Kỳ', 'Hội An', 'Điện Bàn', 'Đại Lộc', 'Duy Xuyên',
        'Hiệp Đức', 'Nam Giang', 'Nam Trà My', 'Nông Sơn', 'Núi Thành',
        'Phú Ninh', 'Phước Sơn', 'Quế Sơn', 'Tây Giang', 'Thăng Bình',
        'Tiên Phước', 'Bắc Trà My'
    ],
    'Quảng Ngãi': [
        'TP. Quảng Ngãi', 'Ba Tơ', 'Bình Sơn', 'Đức Phổ', 'Lý Sơn',
        'Minh Long', 'Mộ Đức', 'Nghĩa Hành', 'Sơn Hà', 'Sơn Tây',
        'Sơn Tịnh', 'Trà Bồng', 'Tư Nghĩa'
    ],
    'Phú Yên': [
        'Tuy Hòa', 'Sông Cầu', 'Đông Hòa', 'Đồng Xuân', 'Phú Hòa',
        'Sơn Hòa', 'Sông Hinh', 'Tây Hòa', 'Tuy An'
    ],
    'Ninh Thuận': [
        'Phan Rang - Tháp Chàm', 'Bác Ái', 'Ninh Hải', 'Ninh Phước',
        'Ninh Sơn', 'Thuận Bắc', 'Thuận Nam'
    ],
    'Bình Thuận': [
        'Phan Thiết', 'La Gi', 'Bắc Bình', 'Đức Linh', 'Hàm Tân',
        'Hàm Thuận Bắc', 'Hàm Thuận Nam', 'Phú Quý', 'Tánh Linh', 'Tuy Phong'
    ],
    'Kon Tum': [
        'TP. Kon Tum', 'Đắk Glei', 'Đắk Hà', 'Đắk Tô', 'Ia H\'Drai',
        'Kon Plông', 'Kon Rẫy', 'Ngọc Hồi', 'Sa Thầy', 'Tu Mơ Rông'
    ],
    'Gia Lai': [
        'Pleiku', 'An Khê', 'Ayun Pa', 'Chư Păh', 'Chư Prông', 'Chư Pưh',
        'Chư Sê', 'Đắk Đoa', 'Đắk Pơ', 'Đức Cơ', 'Ia Grai', 'Ia Pa',
        'K\'Bang', 'Kông Chro', 'Krông Pa', 'Mang Yang', 'Phú Thiện'
    ],
    'Đắk Lắk': [
        'Buôn Ma Thuột', 'Buôn Hồ', 'Buôn Đôn', 'Cư Kuin', 'Cư M\'gar',
        'Ea H\'leo', 'Ea Kar', 'Ea Súp', 'Krông Ana', 'Krông Bông',
        'Krông Búk', 'Krông Năng', 'Krông Pắc', 'Lắk', 'M\'Drắk'
    ],
    'Đắk Nông': [
        'Gia Nghĩa', 'Cư Jút', 'Đắk Glong', 'Đắk Mil', 'Đắk R\'lấp',
        'Đắk Song', 'Krông Nô', 'Tuy Đức'
    ],
    'Tây Ninh': [
        'TP. Tây Ninh', 'Hòa Thành', 'Trảng Bàng', 'Bến Cầu', 'Châu Thành',
        'Dương Minh Châu', 'Gò Dầu', 'Tân Biên', 'Tân Châu'
    ],
    'Bình Phước': [
        'Đồng Xoài', 'Bình Long', 'Phước Long', 'Bù Đăng', 'Bù Đốp',
        'Bù Gia Mập', 'Chơn Thành', 'Đồng Phú', 'Hớn Quản', 'Lộc Ninh', 'Phú Riềng'
    ],
    'Long An': [
        'Tân An', 'Kiến Tường', 'Bến Lức', 'Cần Đước', 'Cần Giuộc',
        'Châu Thành', 'Đức Hòa', 'Đức Huệ', 'Mộc Hóa', 'Tân Hưng',
        'Tân Thạnh', 'Tân Trụ', 'Thạnh Hóa', 'Thủ Thừa', 'Vĩnh Hưng'
    ],
    'Bến Tre': [
        'TP. Bến Tre', 'Ba Tri', 'Bình Đại', 'Châu Thành', 'Chợ Lách',
        'Giồng Trôm', 'Mỏ Cày Bắc', 'Mỏ Cày Nam', 'Thạnh Phú'
    ],
    'Trà Vinh': [
        'TP. Trà Vinh', 'Duyên Hải', 'Càng Long', 'Cầu Kè', 'Cầu Ngang',
        'Châu Thành', 'Tiểu Cần', 'Trà Cú'
    ],
    'Hậu Giang': [
        'Vị Thanh', 'Ngã Bảy', 'Long Mỹ', 'Châu Thành', 'Châu Thành A',
        'Phụng Hiệp', 'Vị Thủy'
    ],
    'Sóc Trăng': [
        'TP. Sóc Trăng', 'Ngã Năm', 'Vĩnh Châu', 'Châu Thành', 'Cù Lao Dung',
        'Kế Sách', 'Long Phú', 'Mỹ Tú', 'Mỹ Xuyên', 'Thạnh Trị', 'Trần Đề'
    ],
    'Bạc Liêu': [
        'TP. Bạc Liêu', 'Giá Rai', 'Đông Hải', 'Hòa Bình', 'Hồng Dân',
        'Phước Long', 'Vĩnh Lợi'
    ],
    'Cà Mau': [
        'TP. Cà Mau', 'Cái Nước', 'Đầm Dơi', 'Năm Căn', 'Ngọc Hiển',
        'Phú Tân', 'Thới Bình', 'Trần Văn Thời', 'U Minh'
    ],
}

