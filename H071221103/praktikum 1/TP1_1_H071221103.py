print ('menghitung jumlah tagihan listrik bulanan')

nilai = input('rata-rata pemakaian listrik perhari :')
tarif_listrik = float (1325)
wh = float(nilai)

#mengubah wh ke kwh#
harian = float(wh/1000)
bulanan = float (harian*30)
harga = float (bulanan*tarif_listrik)


print ('jumlah tagihan listrik bulanan = Rp',  harga)



