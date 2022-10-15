print ("program mengubah derajat ke waktu")
while True:
    derajat = input('masukkan derajat = ')
    if derajat == 'end' or derajat == 'exit':
        break
    else :
        totaldetik = 1/15*3600*float(derajat)



        jam = ((totaldetik // 3600) + 6) % 24
        menit = (totaldetik % 3600 / 60)
        detik = (totaldetik % 3600 % 60)

        if jam >= 6 and jam < 11:
            print('selamat pagi')
        elif jam >= 11 and jam <= 15:
            print('selamat siang')
        elif jam > 15 and jam <= 18:
            print('selamat sore')
        elif jam > 18 and jam <= 24:
            print('selamat malam')
        else :
            print('selamat malam')

        print('{:02d}:{:02d}:{:02d}'.format (int(jam), int(menit), int(detik)))
          
