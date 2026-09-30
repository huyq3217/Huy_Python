# Bài tập 1.1:

# 1. Hàm tìm ước số chung lớn nhất (USCLN)
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 2. Hàm tìm bội số chung nhỏ nhất (BSCNN)
def bscnn(a, b):
    return a * b // uscln(a, b)


# 3. Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 4. Hàm kiểm tra số hoàn thiện
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0

    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n


# =========================
# GỌI HÀM THỬ
# =========================

print("=== USCLN ===")
print(uscln(24, 36))     # Kết quả: 12
print(uscln(15, 25))     # Kết quả: 5
print(uscln(18, 30))     # Kết quả: 6


print("\n=== BSCNN ===")
print(bscnn(4, 6))       # Kết quả: 12
print(bscnn(5, 10))      # Kết quả: 10
print(bscnn(8, 12))      # Kết quả: 24


print("\n=== KIỂM TRA SỐ NGUYÊN TỐ ===")
print(kiem_tra_nguyen_to(29))  # True
print(kiem_tra_nguyen_to(17))  # True
print(kiem_tra_nguyen_to(20))  # False


print("\n=== KIỂM TRA SỐ HOÀN THIỆN ===")
print(kiem_tra_so_hoan_thien(6))    # True
print(kiem_tra_so_hoan_thien(28))   # True
print(kiem_tra_so_hoan_thien(20))   # False
# Bài tập 1.2
def in_loi_chao(ten):
 print(f"Xin chao, {ten}!")
 return # ham khong tra ve gia tri (tra ve None)
def chia_lay_thuong_du(a, b):
 return a // b, a % b # tra ve nhieu gia tri qua tuple
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")
# Bài tập 2
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
 print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")
gioi_thieu("An") # dung het gia tri mac dinh
gioi_thieu("Binh", 20) # ghi de tuoi
gioi_thieu("Chi", lop="CNTT01") # dung tham so tu khoa, bo qua tuoi
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19) # thu tu tham so tu khoa co the dao lon
# Bài tập 3.1 
def tinh_tong(*args):
 tong = 0
 for so in args:
  tong += so
 return tong
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong()) # khong truyen so nao -> tra ve 0
#Bài tập 3.2 – **kwargs: in thông tin động:
def in_thong_tin(ho_ten, tuoi, **kwargs):

 print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
 for khoa, gia_tri in kwargs.items():
  print(f" {khoa}: {gia_tri}")
in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")

'''
Yêu cầu: Giải thích vì sao khi gọi hàm bằng tham số từ khóa (ten=..., lop=...) thì thứ tự truyền vào không
quan trọng: Khi gọi hàm bằng tham số từ khóa như ten=..., lop=..., 
Python sẽ dựa vào tên của tham số để xác định giá trị cần truyền vào,
thay vì dựa vào vị trí của tham số. Vì vậy, thứ tự truyền các tham số 
không quan trọng. Ví dụ, nếu hàm có dạng hien_thi(ten, lop) thì ta có thể gọi
hien_thi(ten="An", lop="DH14C5") hoặc hien_thi(lop="DH14C5", ten="An"), cả hai
cách đều cho kết quả giống nhau. Điều này giúp việc gọi hàm dễ đọc, rõ ràng và hạn 
chế nhầm lẫn khi hàm có nhiều tham số.


'''