# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:05:12 2024

@author: ACER
"""

ngay = int(input("Nhập vào ngày sinh của bạn: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
# Dạng a: Ngày/tháng/năm
print("Định dạng a: ", ngay, "/", thang, "/", nam, sep="")
# Dạng b: Ngày/tháng/năm (năm 2 chữ số cuối)
print("Định dạng b: ", ngay, "/", thang, "/", str(nam)[-2:], sep="")
# Dạng c: Năm/tháng/ngày
print("Định dạng c: ", nam, "/", thang, "/", ngay, sep="")
# Dạng ngược lại
print("Định dạng ngược lại (c -> b -> a):")
print(str(nam)[-2:], "/", thang, "/", ngay, sep="")
print(nam, "/", thang, "/", ngay, sep="")
print(ngay, "/", thang, "/", nam, sep="")
