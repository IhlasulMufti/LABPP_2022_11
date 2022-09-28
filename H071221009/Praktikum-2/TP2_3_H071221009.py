print("===============================================================")
print("       Program menentukan nilai terbesar dari tiga angka       ")
print("===============================================================")

a = int(input('Masukkan nilai a: '))
b = int(input('Masukkan nilai b: '))
c = int(input('Masukkan nilai c: '))

if a > b and a > c:
    print(a, "adalah nilai terbesar")
elif b > a and b > c:
    print(b, "adalah nilai terbesar")
else:
    print(c, "adalah nilai terbesar")