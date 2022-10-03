# program mencetak angka #

x = int(input("Masukkan angka baris horizontal: "))
y = int(input("Masukkan angka baris vertikal: "))
if x < y:
    for i in range(1, y + 1):
        print(i, end=" ") 
        if i % x == 0: 
            print()
else:
    print("Data tidak valid")