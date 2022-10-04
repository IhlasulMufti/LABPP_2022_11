x = int(input("masukkan nilai x : "))  # x itu horizontal
y = int(input("masukkan nilai y : "))  # y vertikal
angka = 1
if x < y:
    while angka <= y:
        for u in range(x):
            if angka > y:
                break
            else:
                print(angka, end=" ")
                angka = angka + 1
        print()
else:
    print("inputan salah")
