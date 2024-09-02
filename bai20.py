# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:14:15 2024

@author: ACER
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("Số có giá trị lớn nhất là:", max_num)
