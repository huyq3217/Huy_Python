quan_ly_diem = {
    "Nguyen Van A": [8.0, 7.5, 9.0],
    "Tran Thi B": [6.6, 5.5, 5.5],
    "Le Van C": [9.0, 8.5, 8.1]
}

quan_ly_diem["Pham Thi D"] = [7.0, 8.0, 7.5]
quan_ly_diem["Tran Thi B"][0] = 7.0

diem_trung_binh = {}

for ho_ten, danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten] = round(
        sum(danh_sach_diem) / len(danh_sach_diem), 2
    )
print("BANG DIEM TRUNG BINH:")

for ho_ten, diem_tb in diem_trung_binh.items():
    dat_loai_gioi = diem_tb >= 8.0
    print(f"{ho_ten}: {diem_tb} - Dat loai Gioi: {dat_loai_gioi}")