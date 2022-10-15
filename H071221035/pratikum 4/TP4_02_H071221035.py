# Program Python untuk menemukan FPB dua buah bilangan

def hitung_FPB(angka_pertama,angka_kedua):
# memilih bilangan yang paling kecil
    if angka_pertama > angka_kedua:
        lebihkecil = angka_kedua
    else:
        lebihkecil = angka_pertama
    for i in range(1, lebihkecil+1): #tambah 1 biar perulangan berlanjut
        if((angka_pertama % i == 0) and (angka_kedua % i == 0)):
            fpb = i
    return fpb

angka_pertama = int(input("masukkan angka pertama: "))
angka_kedua = int(input("masukkan angka kedua: "))

# print("FPB dari", angka_pertama,"dan", angka_kedua,"=", hitung_FPB(angka_pertama, angka_kedua))
print(f"fpb dari {angka_pertama} dan {angka_kedua}= {hitung_FPB(angka_pertama,angka_kedua)}")