# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:15:29 2024

@author: ACER
"""

import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
tu_so = (a + b) / (math.pow(a, 1/3) + math.pow(b, 1/3)) - math.pow(a*b, 1/3)
mau_so = math.pow(math.pow(a, 1/3) - math.pow(b, 1/3), 2)
if mau_so == 0:
    print("Mẫu số bằng 0. Không thể tính toán.")
else:
    ket_qua = tu_so / mau_so
    print("Kết quả của biểu thức là:", ket_qua)
    
    