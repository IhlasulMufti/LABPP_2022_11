n = float(input('Masukkan nilai derajat yang akan dikonversi : '))

jam   = 6
menit = 0
hari  = 24*3600
detik = round((n/360)*hari)

while detik >= 3600:
    detik   -=3600
    jam     +=1

while detik >= 60 :
    detik   -= 60
    menit   += 1

jam %= 24

if jam < 4:
    print('selamat malam')
elif jam <= 10:
    print('selamat pagi')
elif jam <= 14:
    print('selamat siang')
elif jam <= 18:
    print('selamat sore')
elif jam <= 24:
    print('selamat malam')

print ("%02d:%02d:%02d"%(jam,menit,detik))