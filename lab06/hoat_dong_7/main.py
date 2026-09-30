import utils
print(utils.dao_nguoc_chuoi("Python"))
print(utils.kiem_tra_palindrome("madam"))
print(utils.chuan_hoa_ho_ten(" nguyen van an "))
print(utils.uscln(24, 36))
print(utils.kiem_tra_nguyen_to(29))

'''
Yêu cầu: Giải thích vì sao utils.py và main.py cần đặt trong 
cùng một thư mục để lệnh import utils hoạt động
đúng.utils.py và main.py cần đặt trong cùng một thư mục để Python 
có thể dễ dàng tìm thấy module utils khi thực hiện lệnh import utils.
 Khi chạy main.py, Python sẽ tìm file utils.py trong thư mục hiện tại và 
 nạp các hàm, biến có trong file đó để sử dụng. Nếu hai file nằm ở hai thư mục khác nhau,
  Python có thể không tìm thấy utils.py và sẽ báo lỗi ModuleNotFoundError. Vì vậy
  , đặt hai file cùng thư mục giúp việc import module đơn giản và chương trình hoạt động đúng.
ư
'''