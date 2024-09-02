# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:40:25 2024

@author: ACER
"""

thoigian1= input("Nhập giờ phút giây (VD:1h8p8s): ")
giomot= int(thoigian1.split("h")[0])
phutmot=int(thoigian1.split("h")[1].split("p")[0])
giaymot=int(thoigian1.split("p")[1].split("s")[0])
h=giomot*3600
p=phutmot*60
giayy=giaymot
doisanggiay= h+p+giayy
thoigian2= input("Nhập giờ phút giây (VD:1h8p8s): ")
giohai= int(thoigian2.split("h")[0])
phuthai=int(thoigian2.split("h")[1].split("p")[0])
giayhai=int(thoigian2.split("p")[1].split("s")[0])
gio= giohai*3600
phut= phuthai*60
giay=giayhai
doisanggiayy= gio+phut+giay
conghaithoigian= doisanggiay+ doisanggiayy
print("Kết quả của cộng hai giây là: ", conghaithoigian, "giây")
if doisanggiay>=doisanggiayy:
    ketqua= doisanggiay-doisanggiayy
    print("Kết quả của trừ hai giây là: ",ketqua, "giây")
else:
    ketqua=doisanggiayy-doisanggiay
    print("Kết quả của trừ hai giây là: ",ketqua, "giây")
    



