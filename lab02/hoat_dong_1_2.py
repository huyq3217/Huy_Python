#bai_1.1
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))
"""
Trả lời: Vì họ tên bản chất vốn là văn bản,
 nên khi nhập vào sẽ được lưu dưới dạng chuỗi (string).
Năm sinh là một con số nguyên, nên khi nhập vào sẽ 
được lưu dưới dạng số nguyên (int).
 Điểm trung bình là một con số thực, nên khi nhập
  vào sẽ được lưu dưới dạng số thực (float).
"""
#bai_1.2
print("Python", "la", "ngon", "ngu", "lap trinh", sep="")
print("Python", "la", "ngon", "ngu", "lap trinh", sep=",")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="'")
print("Python", "la", "ngon", "ngu", "lap trinh", sep=" \n")

"""Trả lời:
- sep="" : không có khoảng trắng giữa các từ
- sep="," : có dấu phẩy giữa các từ
- sep="'" : có dấu nháy đơn giữa các từ
- sep=" \n" : có khoảng trắng và xuống dòng giữa các từ"""

print("Dong 1", end=" | ")
print("Dong 2")
#bai_1.3
# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
# str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))
# toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))
"""
Giai thich:
Ca 3 cach deu cho ket qua giong nhau.
f-string duoc khuyen khich dung vi:
- Cu phap ngan gon.
- De doc, de hieu.
- Chen bien truc tiep vao chuoi.
- De dinh dang so"""
#Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""

ho_ten = "Tran Thi B" # bien luu ho ten
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)
"""
S4 và S5: S4 la chuoi binh thuong, S5 la chuoi raw (khong can escape ky tu dac biet)
raw string dùng khi lam viec voi duong dan file, regex, hay cac ky tu dac biet.
"""