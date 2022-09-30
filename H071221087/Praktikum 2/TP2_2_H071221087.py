golongan = (input('golongan = '))
daya = int(input('daya = '))
pemakaian = int(input('pemakaian = '))

print( 30*"=" )

if golongan == "R1":
    if daya == 900:
        print('jumlah tagihan anda :', pemakaian * 1352)
    elif daya == 1300 and 2200:
        print('jumlah tagihan anda :', pemakaian * 1444.70)
    else:
        print('data tidak valid')    
elif golongan == "R2":
    if daya >= 3500 and daya <= 5000:
        print('jumlah tagihan anda :', pemakaian * 1699.53)
    else:
        print('data tidak valid')    
elif golongan == 'R3':
    if daya >= 6600:
        print('jumlah tagihan anda', pemakaian * 1699.53)
    else:
        print('data tidak valid')    
elif golongan == 'B2':
    if daya >= 6600 and daya <= 200000:
        print('jumlah tagihan anda :', pemakaian * 1444.70)
    else:
        print('data tidak valid')    
elif golongan == "B3":
    if daya >= 200000:
        print('jumlah tagihan anda :', pemakaian * 1114.74)
    else:
        print('data tidak valid')
elif golongan == "I3":
    if daya >= 200000:
        print('jumlah tagihan anda :', pemakaian * 1314.12)
    else:
        print('data tidak valid')
elif golongan == "P1":
    if daya >= 6600 and daya <= 200000:
        print('jumlah tagihan anda :', pemakaian * 1523.28)
    else:
        print('data tidak valid')              
else:
    print('data tidak valid')