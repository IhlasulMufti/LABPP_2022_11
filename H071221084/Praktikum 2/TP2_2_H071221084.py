tarif_R1_1 = 1352
tarif_R1_2 = 1444.70
tarif_R1_3 = 1444.70
tarif_R2   = 1699.53
tarif_R3   = 1352
tarif_B2   = 1444.70
tarif_B3   = 1114.74
tarif_I3   = 1314.12
tarif_P1   = 1352

golongan   =       input("Golongan  : ").upper()
daya       = float(input("Daya      : "))
pemakaian  = float(input("Pemakaian : "))

if golongan   == 'R1':
    if daya   == 900:
        print(f"Jumlah tagihan Anda : Rp.{tarif_R1_1 * pemakaian:_}".replace('.',',').replace('_','.'))
    elif daya == 1300:
        print(f"Jumlah tagihan Anda : Rp.{tarif_R1_2 * pemakaian:_}".replace('.',',').replace('_','.'))
    elif daya == 2200:
        print(f"Jumlah tagihan Anda : Rp.{tarif_R1_3 * pemakaian:_}".replace('.',',').replace('_','.'))
elif golongan == 'R2':
    if daya   >= 3500 and daya <= 5500:
        print(f"Jumlah tagihan Anda : Rp.{tarif_R2 * pemakaian:_}".replace('.',',').replace('_','.'))
elif golongan == 'R3':
    if daya   >= 6600 :
        print(f"Jumlah tagihan Anda : Rp.{tarif_R3 * pemakaian:_}".replace('.',',').replace('_','.'))
elif golongan == 'B2':
    if daya   >= 6600 and daya <= 200000:
        print(f"Jumlah tagihan Anda : Rp.{tarif_B2 * pemakaian:_}".replace('.',',').replace('_','.'))
elif golongan == 'B3':
    if daya > 200000 :
        print(f"Jumlah tagihan Anda : Rp.{tarif_B3 * pemakaian:_}".replace('.',',').replace('_','.'))
elif golongan == 'I3':
    if daya   >= 200000:
        print(f"Jumlah tagihan Anda : Rp.{tarif_I3 * pemakaian:_.2f}".replace('.',',').replace('_','.'))
elif golongan == 'P1':
    if daya   >= 6600 and daya <= 200000:
        print(f"Jumlah tagihan Anda : Rp.{tarif_P1 * pemakaian:_}".replace('.',',').replace('_','.'))
else:
    print("Input tidak Valid!")






