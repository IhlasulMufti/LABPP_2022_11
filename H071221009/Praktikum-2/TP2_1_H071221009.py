print("===============================================================")
print("      Program konversi nilai dalam bentuk angka ke huruf       ")
print("===============================================================")

nilai = int(input("Masukkan nilai dalam angka : "))
if nilai >= 90 and nilai <= 100: 
    hasil = 'A'
elif nilai >= 80 and nilai < 90:
    hasil = 'B'
elif nilai >= 70 and nilai < 80:
    hasil = 'C'
elif nilai >= 60 and nilai < 70:
    hasil = 'D'
elif nilai >= 40 and nilai < 60:
    hasil = 'E'
elif nilai < 40 and nilai >= 0:
    hasil = 'F'
else:
    hasil = "inputan salah, masukkan nilai 0-100"

print("nilai {} = '{}'". format (nilai,hasil))