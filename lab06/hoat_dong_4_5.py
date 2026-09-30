#hoạt động 4
so_luot_truy_cap = 0 
def tang_luot_truy_cap():
 global so_luot_truy_cap
so_luot_truy_cap += 1
def vi_du_bien_local():
 so_luot_truy_cap = 100 
print("Ben trong ham, bien local =", so_luot_truy_cap)
tang_luot_truy_cap()
tang_luot_truy_cap()
print("So luot truy cap (global):", so_luot_truy_cap)
vi_du_bien_local()
print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)
#hoạt động 5
#bài 5.1
danh_sach_so = [1, 2, 3, 4, 5]
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print(binh_phuong)
#bài 5.2
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print(so_chan)
#bài 5.3
danh_sach_sv = [
{"ten": "An", "diem": 8.5},

{"ten": "Binh", "diem": 7.0},
{"ten": "Chi", "diem": 9.2},
]
sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)
for sv in sap_xep_theo_diem:
 print(sv["ten"], "-", sv["diem"])
print("--- Giam dan ---")
for sv in sap_xep_giam_dan:
 print(sv["ten"], "-", sv["diem"])

 '''
Yêu cầu: Giải thích vì sao nếu bỏ dòng global so_luot_truy_cap trong hàm tang_luot_truy_cap(), chương
trình sẽ báo lỗi UnboundLocalError.: Trong Python, biến được tạo bên trong hàm mặc
 định được xem là biến cục bộ của hàm đó. Khi hàm tang_luot_truy_cap() thực hiện phép
tăng như so_luot_truy_cap += 1, Python hiểu rằng so_luot_truy_cap là biến cục bộ.
Tuy nhiên, biến này chưa được gán giá trị trong hàm mà lại được sử dụng trước, 
nên chương trình báo lỗi UnboundLocalError. Dòng global so_luot_truy_cap dùng để 
thông báo cho Python rằng biến so_luot_truy_cap là biến toàn cục đã được khai báo bên
ngoài hàm, từ đó hàm có thể thay đổi trực tiếp giá trị của biến đó.

Yêu cầu: So sánh cách sắp xếp này với cách "đặt điểm trước tên trong tuple" đã 
dùng ở Buổi 3 — vì sao
dùng key=lambda linh hoạt hơn? Cách “đặt điểm trước tên trong tuple” 
sắp xếp dựa vào phần tử đầu tiên của tuple, nên muốn sắp xếp theo tiêu chí 
khác thì phải thay đổi cách tổ chức dữ liệu. Trong khi đó, dùng key=lambda 
cho phép ta chỉ định trực tiếp thuộc tính hoặc tiêu chí muốn dùng để sắp xếp 
mà không cần thay đổi dữ liệu ban đầu. Vì vậy, key=lambda linh hoạt hơn, có thể 
sắp xếp theo điểm, tên, tuổi hoặc nhiều tiêu chí khác nhau một cách dễ dàng.
 '''