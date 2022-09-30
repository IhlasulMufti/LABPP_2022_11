print("Konfersi Nilai Angka Ke Dalam Bentuk Huruf")

nilai = int(input("Masukkan Angka : "))

if nilai >= 90 and nilai <=100:
    print(f"Nilai {nilai} = A")
elif nilai >= 80 and nilai <90:
    print(f"Nilai {nilai} = B")
elif nilai >= 70 and nilai <80:
    print(f"Nilai {nilai} = C")
elif nilai >= 60 and nilai <70:
    print(f"Nilai {nilai} = D")
elif nilai >= 40 and nilai <60:
    print(f"Nilai {nilai} = E")
elif nilai < 40 and nilai >= 0:
    print(f"Nilai {nilai} = F")
else:
    print("Nilai Tidak Valid")
