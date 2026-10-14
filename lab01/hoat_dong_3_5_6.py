#Hoạt động 3 - Đặng Quốc Huy - 2411062615
#3.1
#định dạng sai :
# 1diem - bắt đầu bằng chữ số
# gia-tri - chứa ký tự gạch ngang, python hiểu là trừ
# Diem TB - chứa dấu cách
# class - trùng từ khóa bảo lưu của python
# so luong - chứa dấu cách
# 2024_data - bắt đầu bằng chữ số
# tong$ - có chứa ký tự đặc biệt
#định dạng hợp lệ :
#_tam_thoi
#MAX_SPEED
#diemTB
#sinhVien1
#3.2
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000
print("Họ và tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)
#hoạt động 5
#5.1
a = 17
b = 5
print("a + b  =", a + b)   
print("a - b  =", a - b)   
print("a * b  =", a * b)   
print("a / b  =", a / b)   
print("a // b =", a // b)  
print("a % b  =", a % b)   
print("a ** b =", a ** b) 
#5.2
diem = 6.5
tuoi = 20

# Kiểm tra điểm đạt loại Khá (từ 6.5 đến dưới 8.0) dùng 'and'
la_loai_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá:", la_loai_kha)  # True

# Kiểm tra tuổi chưa đủ 18 hoặc trên 60 dùng 'or'
chua_du_18_hoac_tren_60 = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60:", chua_du_18_hoac_tren_60)  # False

# Phủ định lại điều kiện trên bằng 'not'
phu_dinh_tuoi = not ((tuoi < 18) or (tuoi > 60))
# Trong độ tuổi lao động từ 18 đến 60
print("Phủ định điều kiện tuổi (18 <= tuổi <= 60):", phu_dinh_tuoi)  # True

#5.3
# Chuỗi toán tử gán mở rộng
x = 10
print("Ban đầu: x =", x)
x += 5   # x = 10 + 5 = 15
print("Sau khi x += 5 :", x)
x -= 3   # x = 15 - 3 = 12
print("Sau khi x -= 3 :", x)
x *= 2   # x = 12 * 2 = 24
print("Sau khi x *= 2 :", x)
x /= 4   # x = 24 / 4 = 6.0 (chuyển sang float)
print("Sau khi x /= 4 :", x)
x //= 2  # x = 6.0 // 2 = 3.0
print("Sau khi x //= 2:", x)
x **= 3  # x = 3.0 ** 3 = 27.0
print("Sau khi x **= 3:", x)
print("-" * 30)

# Toán tử thành viên (in) và toán tử đồng nhất (is)
danh_sach = [1, 2, 3, "python"]

# Toán tử 'in': kiểm tra xem phần tử có nằm trong tập hợp hay không
co_chua_3 = 3 in danh_sach
print("Số 3 có trong danh_sach không?", co_chua_3)  # True

# Toán tử 'is': kiểm tra 2 biến có cùng trỏ tới 1 ô nhớ (đối tượng) hay không
danh_sach_2 = danh_sach        # danh_sach_2 cùng tham chiếu tới ô nhớ của danh_sach
danh_sach_3 = [1, 2, 3, "python"] # Danh sách mới có cùng giá trị nhưng ô nhớ khác

print("danh_sach_2 is danh_sach:", danh_sach_2 is danh_sach)  # True (cùng ô nhớ)
print("danh_sach_3 is danh_sach:", danh_sach_3 is danh_sach)  # False (khác ô nhớ dù cùng giá trị ==)

#5.4
# Kiểm tra kết quả thực tế
print("Kết quả 1:", 2 + 3 * 4 ** 2)                  # 50
print("Kết quả 2:", (2 + 3) * 4 ** 2)                # 80
print("Kết quả 3:", 10 > 5 and 3 < 1 or not False)   # True

#hoat dong 6
#6.1
# Gán số nguyên (int)
bien = 10
print(bien, type(bien))

# Gán lại thành chuỗi ký tự (str)
bien = "Xin chao"
print(bien, type(bien))

# Gán lại thành số thực (float)
bien = 3.14
print(bien, type(bien))

# Gán lại thành giá trị logic (bool)
bien = True
print(bien, type(bien))
#6.2
# 1. Khai báo thông tin học sinh và điểm số
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

# 2. Tính điểm trung bình (toán tử số học)
dtb = (diem_toan + diem_ly + diem_hoa) / 3

# 3. Kiểm tra điều kiện xếp loại (toán tử so sánh & logic)
la_gioi = dtb >= 8.0
la_kha = (dtb >= 6.5) and (dtb < 8.0)
la_trung_binh = (dtb >= 5.0) and (dtb < 6.5)
la_yeu = dtb < 5.0

# 4. Xuất kết quả và kiểm tra kiểu dữ liệu bool
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?      :", la_gioi)
print("Dat loai Kha?       :", la_kha)
print("Dat loai Trung binh?:", la_trung_binh)
print("Dat loai Yeu?       :", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))