# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:57:45 2024

@author: ACER
"""
import math 
ban_kinh = float(input("Nhập vào bán kính hình tròn: "))
chu_vi = 2 * math.pi * ban_kinh 
dien_tich = math.pi * ban_kinh**2 
print(f"Chu vi hình tròn là: {chu_vi:.2f}")
print(f"Diện tích hình tròn là: {dien_tich:.2f}")


