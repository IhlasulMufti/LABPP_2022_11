Nilai = int(input("Masukkan Angka :"))

if Nilai >= 90 and Nilai <= 100:
    print("Nilai", Nilai, "= A")
elif Nilai >= 80 and Nilai < 90:
    print("Nilai", Nilai, "= B")
elif Nilai >= 70 and Nilai < 80:
    print("Nilai", Nilai, "= C")
elif Nilai >= 60 and Nilai < 70:
    print("Nilai", Nilai, "= D")
elif Nilai >= 40 and Nilai < 60:
    print("Nilai", Nilai, "= E")
elif Nilai >= 0 and Nilai < 40:
    print("Nilai", Nilai, "= F")
else: 
    print("Nilai tidak valid")
