# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:46:45 2024

@author: ACER
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
temp = 0
if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print("Các số theo thứ tự tăng dần:", a, b, c)   