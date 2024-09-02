# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:20:39 2024

@author: ACER
"""

h = int(input("Nhập vào số giờ (h): "))
p = int(input("Nhập vào số phút (p): "))
s = int(input("Nhập vào số giây (s): "))
tong_so_giay = h * 3600 + p * 60 + s 
print(h,"h", p,"p", s,"s=", tong_so_giay, "giây")
