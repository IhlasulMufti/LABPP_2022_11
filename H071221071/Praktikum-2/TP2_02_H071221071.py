print("MENENTUKAN NILAI TERBESAR DARI TIGA ANGKA")

a = int(input("Masukkan Nilai A : "))
b = int(input("Masukkan Nilai B : "))
c = int(input("Masukkan Nilai C : "))

if a > b and a > c:
    print(f"{a} adalah nilai terbesar")
elif b > a and b > c:
    print(f"{b} adalah nilai terbesar")
elif c > a and c > b:
    print(f"{c} adalah nilai terbesar")

