#Bai1
#Bai1.1
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print(sinh_vien["ho_ten"])             
print(sinh_vien.get("diem_tb"))       
print(sinh_vien.get("lop", "Chua co")) 
#Bai1.2

sinh_vien["lop"] = "CNTT01"       
sinh_vien["diem_tb"] = 9.0       

print(sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")   
print(sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})                                   

print(sinh_vien)

'''Khi dùng sinh_vien[lop],Python yêu cầu phải có key "lop" trong dictionary, nếu không có sẽ báo lỗi KeyError. 
 Còn khi dùng sinh_vien.get("lop"), Python sẽ trả về giá trị None nếu key "lop" không tồn tại, thay vì báo lỗi.'''
#Bai2

diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(diem)

for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")
tong_diem = 0

for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))
#Bai3
#Bai3.1
diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

diem_cong_diem = {
    mon: round(diem + 0.5, 2)
    for mon, diem in diem_mon_hoc.items()
}

print(diem_cong_diem)

ten_mon_viet_hoa = {
    mon.upper(): diem
    for mon, diem in diem_mon_hoc.items()
}

print(ten_mon_viet_hoa)
#Bai3.2

mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print("Giao:", mon_hoc_ky1 & mon_hoc_ky2)

print("Hop:", mon_hoc_ky1 | mon_hoc_ky2)
print("Chi co o ky 1:", mon_hoc_ky1 - mon_hoc_ky2)

'''set không lưu trữ thứ tự, không có phần tử trùng lặp, và không thể thay đổi các phần tử sau khi được tạo ra.
Dictionary lưu trữ dữ liệu theo cặp key-value, cho phép truy cập nhanh chóng thông qua key,
và có thể thay đổi giá trị của các phần tử.
set không cho phép truy cập trực tiếp đến các phần tử thông qua chỉ số, trong khi dictionary cho phép truy cập thông qua key.
sẻ không cho phânf tử trùng lặp vì set là một tập hợp các phần tử duy nhất
trong khi dictionary cho phép các key trùng lặp nhưng giá trị của chúng có thể khác nhau.'''