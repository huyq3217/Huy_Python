# =========================================================
# DỰ ÁN: HỆ THỐNG QUẢN LÝ THƯ VIỆN SÁCH (LIBRARY MANAGEMENT)
# Ngôn ngữ: Python 3.x
# Môi trường: Visual Studio Code
# =========================================================

# ---------------------------------------------------------
# BƯỚC 1: KHỞI TẠO CẤU TRÚC DỮ LIỆU BAN ĐẦU
# ---------------------------------------------------------

# Danh sách lưu trữ toàn bộ thông tin các cuốn sách trong thư viện
danh_sach_sach = [
    {
        "ma_sach": "S01",
        "ten_sach": "Lập trình Python cơ bản",
        "tac_gia": "Nguyễn Văn A",
        "trang_thai": "Sẵn có",
        "nguoi_muon": ""
    },
    {
        "ma_sach": "S02",
        "ten_sach": "Cấu trúc dữ liệu & Giải thuật",
        "tac_gia": "Trần Thị B",
        "trang_thai": "Đã mượn",
        "nguoi_muon": "Lê Văn C"
    },
    {
        "ma_sach": "S03",
        "ten_sach": "Học máy cho người bắt đầu",
        "tac_gia": "Phạm Văn D",
        "trang_thai": "Sẵn có",
        "nguoi_muon": ""
    }
]

# Danh sách lưu lịch sử các giao dịch trả sách để tính doanh thu
lich_su_giao_dich = []


# ---------------------------------------------------------
# BƯỚC 2: HÀM HỖ TRỢ XỬ LÝ LỖI ĐẦU VÀO
# ---------------------------------------------------------

def nhap_so_nguyen(thong_bao):
    """Hàm nhập số nguyên an toàn bằng kỹ thuật try-except"""
    while True:
        try:
            gia_tri = int(input(thong_bao))
            return gia_tri
        except ValueError:
            print(" Lỗi: Vui lòng nhập vào một số nguyên hợp lệ!")


# ---------------------------------------------------------
# BƯỚC 3: XÂY DỰNG CÁC MÔ-ĐUN CHỨC NĂNG
# ---------------------------------------------------------

# Chức năng 1: Hiển thị toàn bộ sách
def hien_thi_tat_ca_sach():
    print("\n" + "="*85)
    print("DANH SÁCH TOÀN BỘ SÁCH TRONG THƯ VIỆN".center(85))
    print("="*85)
    if not danh_sach_sach:
        print("Thư viện hiện chưa có sách nào.")
        return
    
    print(f"{'Mã sách':<10} | {'Tên sách':<30} | {'Tác giả':<20} | {'Trạng thái':<12} | {'Người mượn':<15}")
    print("-" * 85)
    for s in danh_sach_sach:
        nguoi = s['nguoi_muon'] if s['nguoi_muon'] else "-"
        print(f"{s['ma_sach']:<10} | {s['ten_sach']:<30} | {s['tac_gia']:<20} | {s['trang_thai']:<12} | {nguoi:<15}")


# Chức năng 2: Xem nhanh các sách đang sẵn có
def xem_sach_san_co():
    print("\n" + "="*65)
    print("DANH SÁCH SÁCH ĐANG SẴN CÓ (CHƯA AI MƯỢN)".center(65))
    print("="*65)
    sach_co_san = [s for s in danh_sach_sach if s['trang_thai'] == 'Sẵn có']
    if not sach_co_san:
        print("Hiện tại không có sách nào đang sẵn có trong thư viện.")
        return
    
    print(f"{'Mã sách':<10} | {'Tên sách':<30} | {'Tác giả':<20}")
    print("-" * 65)
    for s in sach_co_san:
        print(f"{s['ma_sach']:<10} | {s['ten_sach']:<30} | {s['tac_gia']:<20}")


# Chức năng 3: Thêm sách mới
def them_sach_moi():
    print("\n--- THÊM SÁCH MỚI VÀO THƯ VIỆN ---")
    ma = input("Nhập mã sách mới: ").strip()
    
    # Kiểm tra trùng lặp mã sách
    for s in danh_sach_sach:
        if s['ma_sach'].lower() == ma.lower():
            print(" Lỗi: Mã sách này đã tồn tại trong thư viện!")
            return
            
    ten = input("Nhập tên sách: ").strip()
    tac_gia = input("Nhập tên tác giả: ").strip()
    
    sach_moi = {
        "ma_sach": ma,
        "ten_sach": ten,
        "tac_gia": tac_gia,
        "trang_thai": "Sẵn có",
        "nguoi_muon": ""
    }
    danh_sach_sach.append(sach_moi)
    print(f" Đã thêm thành công sách '{ten}' (Mã: {ma}) vào hệ thống!")


# Chức năng 4: Cho mượn sách
def muon_sach():
    print("\n--- QUẢN LÝ MƯỢN SÁCH ---")
    ma = input("Nhập mã sách khách muốn mượn: ").strip()
    for s in danh_sach_sach:
        if s['ma_sach'].lower() == ma.lower():
            if s['trang_thai'] == 'Đã mượn':
                print(f" Sách '{s['ten_sach']}' đã được mượn bởi độc giả '{s['nguoi_muon']}'.")
                return
            
            ten_nguoi = input("Nhập tên độc giả mượn sách: ").strip()
            s['trang_thai'] = 'Đã mượn'
            s['nguoi_muon'] = ten_nguoi
            print(f" Đã cho độc giả '{ten_nguoi}' mượn thành công sách '{s['ten_sach']}'!")
            return
            
    print(" Lỗi: Không tìm thấy mã sách này trong hệ thống!")


# Chức năng 5: Trả sách và thanh toán phí
def tra_sach():
    print("\n--- TRẢ SÁCH & THANH TOÁN PHÍ MƯỢN ---")
    ma = input("Nhập mã sách khách muốn trả: ").strip()
    for s in danh_sach_sach:
        if s['ma_sach'].lower() == ma.lower():
            if s['trang_thai'] == 'Sẵn có':
                print(" Sách này hiện đang có trong thư viện (chưa ai mượn).")
                return
            
            so_ngay = nhap_so_nguyen("Nhập số ngày đã mượn thực tế: ")
            don_gia_ngay = 5000  # Phí mượn cố định 5.000 VNĐ / ngày
            tong_tien = so_ngay * don_gia_ngay
            
            ten_nguoi = s['nguoi_muon']
            s['trang_thai'] = 'Sẵn có'
            s['nguoi_muon'] = ''
            
            # Ghi nhận vào lịch sử giao dịch
            lich_su_giao_dich.append({
                "ma_sach": s['ma_sach'],
                "ten_sach": s['ten_sach'],
                "nguoi_muon": ten_nguoi,
                "so_ngay": so_ngay,
                "tien_phi": tong_tien
            })
            
            print(f" Đã trả sách '{s['ten_sach']}' thành công!")
            print(f" Độc giả trả: {ten_nguoi}")
            print(f" Phí mượn ({so_ngay} ngày x 5.000 VNĐ): {tong_tien:,} VNĐ")
            return
            
    print("❌ Lỗi: Không tìm thấy mã sách này trong hệ thống!")


# Chức năng 6: Thống kê tổng doanh thu
def thong_ke_doanh_thu():
    print("\n" + "="*80)
    print("THỐNG KÊ DOANH THU MƯỢN SÁCH".center(80))
    print("="*80)
    if not lich_su_giao_dich:
        print("Chưa có giao dịch trả sách nào được ghi nhận.")
        return
    
    tong_doanh_thu = sum(g['tien_phi'] for g in lich_su_giao_dich)
    print(f"{'Mã sách':<10} | {'Tên sách':<25} | {'Người mượn':<15} | {'Số ngày':<10} | {'Phí mượn (VNĐ)':<15}")
    print("-" * 80)
    for g in lich_su_giao_dich:
        print(f"{g['ma_sach']:<10} | {g['ten_sach']:<25} | {g['nguoi_muon']:<15} | {g['so_ngay']:<10} | {g['tien_phi']:<15,}")
    print("-" * 80)
    print(f" TỔNG DOANH THU THU ĐƯỢC: {tong_doanh_thu:,} VNĐ")


# ---------------------------------------------------------
# BƯỚC 4: VÒNG LẶP MENU ĐIỀU HƯỚNG CHÍNH (MAIN LOOP)
# ---------------------------------------------------------

def main():
    while True:
        print("\n" + "="*45)
        print("   HỆ THỐNG QUẢN LÝ THƯ VIỆN SÁCH   ".center(45))
        print("="*45)
        print("1. Hiển thị danh sách toàn bộ sách")
        print("2. Xem nhanh các sách đang sẵn có")
        print("3. Thêm sách mới vào thư viện")
        print("4. Cho mượn sách")
        print("5. Trả sách & thanh toán phí mượn")
        print("6. Thống kê tổng doanh thu")
        print("0. Thoát chương trình")
        print("="*45)
        
        luachon = nhap_so_nguyen("Nhập lựa chọn của bạn (0-6): ")
        
        if luachon == 1:
            hien_thi_tat_ca_sach()
        elif luachon == 2:
            xem_sach_san_co()
        elif luachon == 3:
            them_sach_moi()
        elif luachon == 4:
            muon_sach()
        elif luachon == 5:
            tra_sach()
        elif luachon == 6:
            thong_ke_doanh_thu()
        elif luachon == 0:
            print("\nCảm ơn bạn đã sử dụng phần mềm Quản lý thư viện! Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập từ 0 đến 6.")

# Điểm khởi chạy chương trình
if __name__ == "__main__":
    main()