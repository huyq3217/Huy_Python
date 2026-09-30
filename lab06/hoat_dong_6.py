#bài 6.1
def giai_thua_de_quy(n):
 if n <= 1: # dieu kien dung
  return 1
 return n * giai_thua_de_quy(n - 1)
def giai_thua_lap(n):
 ket_qua = 1
 for i in range(1, n + 1):
    ket_qua *= i
 return ket_qua
print(giai_thua_de_quy(5), "-", giai_thua_lap(5))
#bài 6.2
def fibonacci_de_quy(n):
 if n <= 1: # dieu kien dung
  return n
 return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)
for i in range(10):
 print(fibonacci_de_quy(i), end=" ")
print()

'''
Yêu cầu: Sau khi thực hiện bằng đệ quy, hãy so sánh với vòng 
lặp việc sử dụng vòng lặp: Sau khi thực hiện bằng đệ quy, có thể so 
sánh với cách sử dụng vòng lặp. Đệ quy là cách một hàm tự gọi lại chính nó 
để giải quyết bài toán, giúp code ngắn gọn và dễ hiểu đối với những bài toán có 
cấu trúc lặp lại. Tuy nhiên, đệ quy sử dụng nhiều bộ nhớ hơn và có thể gây lỗi nếu 
gọi quá nhiều lần. Trong khi đó, vòng lặp như for hoặc while thường dễ kiểm soát, ít 
tốn bộ nhớ và phù hợp với các bài toán lặp đơn giản. Vì vậy, vòng lặp thường hiệu quả 
hơn trong những bài toán chỉ cần thực hiện một công việc lặp đi lặp lại.

Yêu cầu: Thử tính fibonacci_de_quy(30), quan sát thời gian chạy chậm hơn hẳn so với
giai_thua_de_quy(30), trả lời vì sao đệ quy Fibonacci "tốn kém" hơn (gợi ý: số lần gọi hàm tăng theo cấp số
nhân do tính lại nhiều lần các giá trị trùng nhau).: Đệ quy Fibonacci tốn kém hơn đệ 
quy giai thừa vì hàm Fibonacci phải gọi lại chính nó nhiều lần và thường tính lại 
các giá trị đã được tính trước đó. Ví dụ, khi tính Fibonacci(30), để tính F(30) phải 
tính F(29) và F(28), sau đó F(29) lại tiếp tục tính F(28) và F(27), khiến nhiều giá trị 
như F(28), F(27), F(26) bị tính lặp lại rất nhiều lần. Vì số lần gọi hàm tăng rất nhanh 
theo cấp số nhân nên thời gian chạy tăng đáng kể. Trong khi đó, giai thừa chỉ có một nhánh 
đệ quy duy nhất, mỗi lần gọi chỉ tính một giá trị tiếp theo nên số lần gọi hàm ít hơn rất nhiều.
'''