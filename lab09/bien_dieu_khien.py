import tkinter as tk

# Khởi tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Vi du bien dieu khien")
cua_so.geometry("350x220")

# Khai báo các biến điều khiển (Control Variables)
bien_ho_ten = tk.StringVar(value="Nguyen Van A")
bien_tuoi = tk.IntVar(value=18)
bien_dong_y_dieu_khoan = tk.BooleanVar(value=False)

# Tạo ô nhập Họ tên
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_ho_ten).grid(row=0, column=1, padx=10, pady=10)

# Tạo ô nhập Tuổi
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_tuoi).grid(row=1, column=1, padx=10, pady=10)

# Tạo hộp chọn Checkbutton
tk.Checkbutton(
    cua_so, text="Dong y dieu khoan", variable=bien_dong_y_dieu_khoan
).grid(row=2, column=0, columnspan=2, pady=10)

# Hàm xử lý lấy giá trị và cập nhật biến
def xem_gia_tri_bien():
    print("Ho ten (StringVar):", bien_ho_ten.get())
    print("Tuoi (IntVar):", bien_tuoi.get())
    print("Dong y dieu khoan (BooleanVar):", bien_dong_y_dieu_khoan.get())
    
    # Sử dụng set() để tăng tuổi lên 1 (ô Entry tuổi trên giao diện sẽ tự cập nhật)
    bien_tuoi.set(bien_tuoi.get() + 1)

# Tạo nút kích hoạt hàm
tk.Button(
    cua_so, text="Xem gia tri bien (va +1 tuoi)", command=xem_gia_tri_bien
).grid(row=3, column=0, columnspan=2, pady=10)

# Vòng lặp giao diện
cua_so.mainloop()