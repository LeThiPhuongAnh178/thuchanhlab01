# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:51:25 2024

@author: ACER
"""

N = int(input("Nhập số nguyên: "))
so_chuoi = str(N)
chu_so = list(so_chuoi)
chu_so.sort()
so_moi = int(''.join(chu_so))
print("Số mới sau khi sắp xếp các chữ số:", so_moi)