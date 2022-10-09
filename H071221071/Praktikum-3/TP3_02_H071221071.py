#Konversi derajat ke jam
while True:
    for x in range(0,360):
        m = (input('M(0-360): '))
        if m == "end" or m == "":
            exit()
        else:
            jam = n // 3600
            jam += 6
            if jam >= 24:
                jam -= 24 #supaya tidak lewat dari 24 jam
            sisa = n % 3600
            menit = sisa // 60
            detik = sisa % 60
            if 0 <= m < 90:
                n = float(m)*240 #1 derajat = 240 detik(3600 x 24/360)
                print('selamat pagi')
                break
            elif 90 <= float(m) < 135:
                n = float(m)*240
                print('selamat siang')
                break
            elif 135 <= float(m) < 180:
                n = float(m)*240
                print('selamat sore')
                break
            elif 180 <= float(m) < 360:
                n = (m)*240
                print('selamat malam')
                break
            else:
                print('hanya menerima inputan 0-360 derajat')
            
            print("%02d:%02d:%02d"%(jam,menit,detik))