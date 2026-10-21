import tkinter as tk
from tkinter import messagebox
cua_so = tk.Tk()
cua_so.title("Chuong trinh chon so thich va loai tai khoan")
cua_so.geometry("400x500")
cua_so.resizable(False, False)
tk.Label(
    cua_so,
    text="CHUONG TRINH LUA CHON",
    font=("Arial", 16, "bold"),
    fg="blue"
).pack(pady=15)
#Bai1
tk.Label(
    cua_so,
    text="1. Chon so thich cua ban:",
    font=("Arial", 12, "bold")
).pack(anchor="w", padx=25, pady=5)

bien_doc_sach = tk.BooleanVar(value=False)
bien_the_thao = tk.BooleanVar(value=False)
bien_am_nhac = tk.BooleanVar(value=False)

tk.Checkbutton(
    cua_so,
    text="Doc sach",
    variable=bien_doc_sach
).pack(anchor="w", padx=45)

tk.Checkbutton(
    cua_so,
    text="The thao",
    variable=bien_the_thao
).pack(anchor="w", padx=45)

tk.Checkbutton(
    cua_so,
    text="Am nhac",
    variable=bien_am_nhac
).pack(anchor="w", padx=45)
#Bai2
tk.Label(
    cua_so,
    text="2. Chon loai tai khoan:",
    font=("Arial", 12, "bold")
).pack(anchor="w", padx=25, pady=10)

bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

tk.Radiobutton(
    cua_so,
    text="Ca nhan",
    variable=bien_loai_tai_khoan,
    value="ca_nhan"
).pack(anchor="w", padx=45)

tk.Radiobutton(
    cua_so,
    text="Doanh nghiep",
    variable=bien_loai_tai_khoan,
    value="doanh_nghiep"
).pack(anchor="w", padx=45)
def xem_lua_chon():
    so_thich = []
    if bien_doc_sach.get():
        so_thich.append("Doc sach")

    if bien_the_thao.get():
        so_thich.append("The thao")

    if bien_am_nhac.get():
        so_thich.append("Am nhac")

    if len(so_thich) == 0:
        so_thich_text = "Chua chon so thich nao"
    else:
        so_thich_text = ", ".join(so_thich)

    if bien_loai_tai_khoan.get() == "ca_nhan":
        loai_tai_khoan = "Ca nhan"
    else:
        loai_tai_khoan = "Doanh nghiep"

    ket_qua = (
        "KET QUA LUA CHON\n\n"
        f"So thich: {so_thich_text}\n"
        f"Loai tai khoan: {loai_tai_khoan}"
    )

    nhan_ket_qua.config(text=ket_qua)

    print("So thich:", so_thich_text)
    print("Loai tai khoan:", loai_tai_khoan)
tk.Button(
    cua_so,
    text="Xac nhan lua chon",
    command=xem_lua_chon,
    bg="lightblue",
    font=("Arial", 11, "bold")
).pack(pady=20)
nhan_ket_qua = tk.Label(
    cua_so,
    text="",
    font=("Arial", 11),
    fg="green",
    justify="left",
    wraplength=350
)
nhan_ket_qua.pack(pady=5)
cua_so.mainloop()