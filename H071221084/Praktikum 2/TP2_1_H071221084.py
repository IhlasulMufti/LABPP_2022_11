nilai = int(input('Masukkan nilai = '))

if nilai >= 90 and nilai <= 100:
    print('Nilai',nilai,'= A')

elif nilai >= 80 and nilai <90:
    print('Nilai',nilai,'= B')

elif nilai >= 70 and nilai <80:
    print('Nilai',nilai,'= C')

elif nilai >= 60 and nilai <70:
    print('Nilai',nilai,'= D')

elif nilai >= 40 and nilai <60:
    print('Nilai',nilai,'= E')

elif nilai < 40 and nilai >=0:
    print('Nilai',nilai,'= F')

else:
    print('Inputan tidak valid')