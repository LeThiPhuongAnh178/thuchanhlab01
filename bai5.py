# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:49:27 2024

@author: ACER
"""

time = input("Nhap vao gio, phut va giay (Theo dinh dang hh:mm:ss): ")
hh, mm, ss = map(int, time. split(":"))
if 0 <= hh < 24 and 0 <= mm < 60 and 0 <= ss < 60:
   Doi = hh*3600 + mm*60 + ss 
   print("So giay la: ", Doi)
else:
    print("Gio, phut va giay chua hop le.")
    
    
    