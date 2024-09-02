# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:17:03 2024

@author: ACER
"""

so = int(input("Nhập một số: "))
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
if 0 <= so <= 9:
    print(chu_so[so])
else:
    print("Không đọc được")
    