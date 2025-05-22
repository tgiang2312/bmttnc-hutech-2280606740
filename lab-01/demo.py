x = 10          #Biến x lưu trữ giá trị số nguyên 10
name = "Alice"  #Biến name lưu trữ chuỗi là "Alice"
is_valid = True #Biến is_valid lưu trữ giá trị boolean true

if = 5 #Lỗi! if là từ khoá, không thể sử dụng làm tên biến

#Cộng(+)
a = 5
b = 3
result =  a + b # Kết quả: 8

#Trừ(-)
a = 8
b = 4
result =  a - b # Kết quả: 4

#Nhân(*)
a = 6
b = 7
result =  a * b # Kết quả: 42

#Chia(/)
a = 20
b = 5
result =  a / b # Kết quả: 4

#Chia lấy phần nguyên(//)
a = 20
b = 3
result =  a // b # Kết quả: 6

#Chia lấy dư(%)
a = 20
b = 7
result =  a - b # Kết quả: 6 (Phần dư của 20 chia cho 7)

#Luỹ thừa(**)
a = 2
b = 3
result =  a ** b # Kết quả: 8 (2^3 = 8)

#Phép toán AND
X = 5
Y = 3
result = (X > 2) and (Y < 4) #Kết quả: True

#Phép toán OR
X = 5
Y = 3
result = (X > 2) or (Y > 4) #Kết quả: True

#Phép toán NOT
X = 5
result = not (X == 5) #Kết quả: False

#Phép so sánh bằng (==)
X = 5
result = (X == 5) #Kết quả: True

#Phép so sánh không bằng (!=)
X = 5
result = (X != 3) #Kết quả: True

#Phép so sánh lớn hơn (>), nhỏ hơn (<)
X = 5
result1 = (X > 3) #Kết quả: True
result2 = (X < 3) #Kết quả: False

#Hàm "input()"
name = input("Nhập tên của bạn: ")
printf("Xin chào, ", name)

#Hàm "print()"
age = 25
print("Tuổi của bạn là: ", age)

# "sep" (ký tự phân cách), "end" (ký tự kết thúc)
print("Python", "là", "ngôn", "ngữ", "lập", "trình", sep="-")
#Kết quả: Python-là-ngôn-ngữ-lập-trình
print("Xin chào", end=" ")
print("Các bạn!") #Kết quả: Xin chào Các bạn!

#Câu lệnh điều kiện (Conditional Statements)
X = 10
if X > 5:
    print("X lớn hơn 5")
elif X == 5:
    print("X bằng 5")
elif X < 5:
    print("X nhỏ hơn 5")

#Vòng lặp "for"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits
    print("fruit")

#Vòng lặp "while"
count = 0
while count < 5:
    print(count)
    count += 1

#Câu lệnh nhảy (Jump Statements) gồm "break", "continue", "pass"
    #"break"
        #Tìm số chia hết cho 5 đầu tiên trong khoảng từ 1 đến 100
for i in range(1,101):
            if i % 5 == 0:
                print("Số chia hết cho 5 đầu tiên là: ", i)
                break
    #"continue"
        #In các số chẵn từ 1 đến 10 và bỏ qua các số lẻ
for i in range(1,11):
            if i % 2 == 0:
                continue
print(i)
    #"pass"
        #Kiểm tra điều kiện, nếu đúng thực hiện, nếu sai thì không làm gì
X = 5
if X > 10:
    print("X lớn hơn 10")
else:
    pass

#Chuỗi
#Khai báo chuỗi trong Python
#Sử dụng dấu ngoặc đơn
string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn.'
# 