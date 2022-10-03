# program menghitung kembalian #

from math import floor
harga_barang = int(input("Masukkan nilai: "))
nilai_uang = int(input("Masukkan nilai: "))
a = int(nilai_uang - harga_barang) 

seratusribu = 0
limapuluh = 0
duapuluh = 0
sepuluhribu = 0
limaribu = 0
duaribu = 0
seribu = 0

if a <= 0 :
    print("Uang tidak cukup")
else:
    while a >= 100000 :
        b = (a // 100000)
        seratusribu = seratusribu + b
        a = a % 100000
    while a >= 50000 :
        b = (a // 50000)
        limapuluh = limapuluh + b
        a = a % 50000
    while a >= 20000 :
        b = (a // 20000)
        duapuluh = duapuluh + b
        a = a % 20000
    while a >= 10000 :
        b = (a // 10000)
        sepuluhribu = sepuluhribu + b
        a = a % 10000
    while a >= 5000 :
        b = (a // 5000)
        limaribu = limaribu + b
        a = a % 5000
    while a >= 2000 :
        b = (a // 2000)
        duaribu = duaribu + b
        a = a % 2000
    while a >= 1000 :
        b = (a // 1000)
        seribu = seribu + b
        a = a % 1000
    print(seratusribu, "uang Rp. 100.000")
    print(limapuluh, "uang Rp. 50.000")
    print(duapuluh, "uang Rp. 20.000")
    print(sepuluhribu, "uang Rp. 10.000")
    print(limaribu, "uang Rp. 5.000")
    print(duaribu, "uang Rp. 2.000")
    print(seribu, "uang Rp. 1.000")