# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:24:19 2024

@author: ACER
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print("Phương trình có nghiệm duy nhất: x =", x)
    