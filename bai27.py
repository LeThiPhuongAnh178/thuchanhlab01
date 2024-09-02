# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:55:54 2024

@author: ACER
"""

import math
hinh = input("Nhập hình (v: vuông, n: chữ nhật, t: tròn): ")
if hinh == 'v':
    canh = float(input("Nhập cạnh hình vuông: "))
    chu_vi = 4 * canh
    dien_tich = canh * canh
    print("Chu vi hình vuông:", chu_vi)
    print("Diện tích hình vuông:", dien_tich)
elif hinh == 'n':
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    chu_vi = 2 * (chieu_dai + chieu_rong)
    dien_tich = chieu_dai * chieu_rong
    print("Chu vi hình chữ nhật:", chu_vi)
    print("Diện tích hình chữ nhật:", dien_tich)
elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * ban_kinh * ban_kinh
    print("Chu vi hình tròn:", chu_vi)
    print("Diện tích hình tròn:", dien_tich)
else:
    print("Hình bạn nhập không hợp lệ!")