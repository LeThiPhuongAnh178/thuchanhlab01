# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:45:09 2024

@author: ACER
"""

chu_cai = input("Nhập một chữ cái: ")
if chu_cai.islower():
    chu_cai_moi = chu_cai.upper()
else:
    chu_cai_moi = chu_cai.lower()
print("Chữ cái mới:", chu_cai_moi)