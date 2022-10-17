print('===========================================')
print (' Program Konversi Nilai Dalam Bentuk Angka')
print('===========================================')

nilai = int(input('masukkan nilai dalam angka : '))

if nilai >= 90: 
    if nilai <= 100:
        hasil = 'A'
    else :
        hasil=('inputan salah')
elif nilai >= 80 and nilai <90:
    hasil = 'B'
elif nilai >= 70 and nilai <80:
    hasil = 'C'
elif nilai >= 60 and nilai <70:
    hasil = 'D'
elif nilai >= 40 and nilai <60:
    hasil = 'E'
elif nilai < 40 and nilai >=0:
    hasil = 'F'
else:
    hasil = 'inputan salah, Masukkan nilai 0-100'

print("nilai {} = '{}'". format (nilai,hasil))