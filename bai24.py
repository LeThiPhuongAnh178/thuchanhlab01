# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:43:12 2024

@author: ACER
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian không hợp lệ.")
    