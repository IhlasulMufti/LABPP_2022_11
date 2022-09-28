print('===============================')
print('   PROGRAM TAGIHAN LISTRIK   ')
print('===============================')

golongan =(input('Golongan = '))
daya = int(input('Daya(VA)= '))
pemakaian = int(input('Pemakaian(kWh) = '))

if golongan == 'R1':
    if daya == 900 :
        print (f'Jumlah tagihan anda : {pemakaian*1352:_}')
    elif daya==1300 :
        print (f'Jumlah tagihan anda : {pemakaian*1444.70:,}')
    elif daya==2200:
        print (f'Jumlah tagihan anda : {pemakaian*1444.70:,}')
    else : 
        print ('Golongan R1 hanya memiliki daya 900, 1300, dan 2200')
elif golongan == 'R2':
    if daya >=3500 and daya<=5500 :
        print (f'Jumlah tagihan anda : {pemakaian*1699.53:,}')
    else :
        print ('Golongan R2 hanya memiliki daya 3500-5500')
elif golongan == 'R3':
    if daya>=6600 :
        print (f'Jumlah tagihan anda : {pemakaian*1699.53:,}')
    else : 
        print ('Golongan R3 hanya memiliki daya 6600')
elif golongan == 'B2':
    if daya>=6600 and daya<=200000:
        print (f'Jumlah tagihan anda : {pemakaian*1444.70:,}')
    else :
        print ('Golongan B2 hanya memiliki daya 6600-200000')
elif golongan == 'B3':
    if daya>200000:
        print (f'Jumlah tagihan anda : {pemakaian*1114.74:,}')
    else :
        print ('Golongan B2 hanya memiliki daya diatas 200000')
elif golongan == 'I3':
    if daya>=200000:
        print (f'Jumlah tagihan anda : {pemakaian*1314.12:,}')
    else : 
        print ('Golongan I3 hanya memiliki daya 200000 keatas')
elif golongan == 'P1':
    if daya>=6600 and daya<=200000:
        print (f'Jumlah tagihan anda : {pemakaian*1523.28:,}')
    else :
        print ('Golongan P1 hanya memiliki daya 6600-200000')
else:
    print ('Data tidak valid')