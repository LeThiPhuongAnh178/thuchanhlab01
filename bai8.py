# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:08:02 2024

@author: ACER
"""

can_nang = float(input("Nhập vào cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập vào chiều cao của bạn (m): "))
bmi = can_nang / (chieu_cao**2)
if bmi < 18.5: 
    print("Bạn đang bị gầy.")
elif 18.5<= bmi <25:
    print("Bạn có cân nặng bình thường.")
elif 25<= bmi <30:
    print("Bạn đang thừa cân.")
else:
    print("Bạn đang bị béo phì.")
print("Chỉ số BMI của bạn là: ", bmi)

