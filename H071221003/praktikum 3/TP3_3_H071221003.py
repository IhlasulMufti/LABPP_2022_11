harga_barang = int(input("Masukkan Harga Barang : " ))
nilai_uang = int(input("Masukkan Nilai Uang : "))
c = int(nilai_uang - harga_barang) 

seratusribu = 0
limapuluh = 0
duapuluh = 0
sepuluhribu = 0
limaribu = 0
duaribu = 0
seribu = 0

if c<=0 :
    print("Tidak ada kembalian")
else :
    while c>=100000 :
        d = (c//100000)
        seratusribu = seratusribu + d
        c = c%100000
    while c>=50000 :
        d = (c//50000)
        limapuluh = limapuluh + d
        c = c%50000
    while c>=20000 :
        d = (c//20000)
        duapuluh = duapuluh + d
        c = c%20000
    while c>=10000 :
        d = (c//10000)
        sepuluhribu = sepuluhribu + d
        c = c%10000
    while c>=5000 :
        d = (c//5000)
        limaribu = limaribu + d
        c = c%5000
    while c>=2000 :
        d = (c//2000)
        duaribu = duaribu + d
        c = c%2000
    while c>=1000 :
        d = (c//1000)
        seribu = seribu + d
        c = c%1000
    print(seratusribu, "uang Rp. 100.000")
    print(limapuluh, "uang Rp. 50.000")
    print(duapuluh, "uang Rp. 20.000")
    print(sepuluhribu, "uang Rp. 10.000")
    print(limaribu, "uang Rp. 5.000")
    print(duaribu, "uang Rp. 2.000")
    print(seribu, "uang Rp. 1.000")