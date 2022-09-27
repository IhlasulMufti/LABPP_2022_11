#PRATIKUM 01 SOAL NO 3
#kwh = wh/1000

nilai = input("rata rata pemakaian listrik harian anda (wh):")
tarif_listrik = 1325 #dalam Kwh
wh = float(nilai)

#mengubah wh ke kwh
harian = float(wh/1000)
bulanan = float(harian * 30)
harga = float(bulanan * tarif_listrik)

print ("jumlah tagihan listrik bulanan anda adalah : Rp.", round(harga, 2))