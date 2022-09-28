##Tugas Praktikum menghitung panjang kapal ##

import math
h = float(input("Masukkan Ketinggian Menara: ")) 
a = float(input("Masukkan Derajat Sudut Ujung Belakang Kapal: "))
b = float(input("Masukkan Derajat Sudut Ujung Depan Kapal: "))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
pjg = belakang-depan

print("Panjang Kapalnya adalah %.1f m" % (pjg))