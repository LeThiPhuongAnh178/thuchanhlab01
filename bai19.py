# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:09:31 2024

@author: ACER
"""

a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
d = int(input("Nhập vào số nguyên d: "))
min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d
print("Số có giá trị nhỏ nhất là:", min_num)

