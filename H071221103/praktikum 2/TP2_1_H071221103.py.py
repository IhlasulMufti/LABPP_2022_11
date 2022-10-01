print ('konversi nilai huruf ke angka')
nilai = input('masukkan nilai :')
nilai = eval (nilai)

if nilai >= 90 and nilai <= 100 :
    na = 'A'

elif nilai >= 80 and nilai < 90 :
    na = 'B'

elif nilai >= 70 and nilai < 80:
   na = 'C'

elif nilai >= 60 and nilai < 70:
    na = 'D'

elif nilai >= 40 and nilai < 60:
    na = 'E'

elif nilai < 40 and nilai >= 0 :
    na = 'F'
else:
    na = ('nilai yang anda masukkan tidak valid')
print (f' nilai {nilai} = {na}')
