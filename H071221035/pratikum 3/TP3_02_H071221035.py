#1 hari = 360 derajat = 24 jam
#15 derajat = 1 jam = 60 menit = 3600 detik
#1 derajat = 4 menit = 240 detik

derajat = float(input('masukkan nilai derajat:'))
waktu_detik = 3600 * derajat /15
if derajat >=0 and derajat <360 :
    jam = int((waktu_detik / 3600) + 6)
    menit = int((waktu_detik / 60 % 60))
    detik = int((waktu_detik % 60))

    if jam < 12 :
        print ('Selamat pagi')
    elif jam >= 12 and jam < 15 :
        print('selamat siang')
    elif jam >= 15 and jam <18 :
        print('selamat sore')
    else:
        print('selamat malam')
    print ("%02d:%02d:%02d"% (jam %24, menit % 60, detik % 60)) #24 untuk batasi
else :
    print("inputan tidak valid")