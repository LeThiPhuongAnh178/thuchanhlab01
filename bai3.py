# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:30:57 2024

@author: ACER
"""
a = int(input("Nhap vao so nguyen duong a: "))
b = int(input("Nhap vao so nguyen duong b: "))
if b==0:
    print("Số chia phải khác 0.")
#Tính phần nguyên và phần dư
phan_nguyen = a//b
phan_du = a%b
#In kết quả
print(f"Phần nguyên của {a} chia cho {b} là: {phan_nguyen}")
print(f"Phần dư của {a} chia cho {b} là: {phan_du}")

