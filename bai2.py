# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:12:38 2024

@author: ACER
"""

a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))
#Kiểm tra trường hợp chia cho 0
if b == 0:
    print("Khong the chia cho 0")
#Tính toán các phép toán
tong = a+b
hieu = a-b
tich = a*b
thuong = a/b
# Làm tròn thương đến 2 và 3 chữ số sau dấu phẩy
thuong_tron_2 = round(thuong, 2)
thuong_tron_3 = round(thuong, 3)
#In kết quả ra màn hình
print("Tổng: ", tong)
print("Hiệu: ", hieu)
print("Tích: ", tich)
print("Thương (Làm tròn 2 chữ số): ", thuong_tron_2)
print("Thương (Làm tròn 3 chữ số): ", thuong_tron_3)
