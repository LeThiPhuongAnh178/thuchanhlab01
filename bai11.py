# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:46:39 2024

@author: ACER
"""

ky_tu_thuong = input("Nhập một ký tự chữ thường: ")
#Kiểm tra xem ký tự nhập vào có phải là chữ thường không
if ky_tu_thuong.islower():
    ky_tu_hoa = ky_tu_thuong.upper()
    print("Ký tự chữ hoa tương ứng là: ", ky_tu_hoa)
else: 
    print("Vui lòng nhập một kỹ tự chữ thường.")
    
    


