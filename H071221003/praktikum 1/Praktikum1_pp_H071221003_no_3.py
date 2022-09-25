print("=====Menghitung Jumlah Tagihan Listrik bulanan=====")
nilai = input("rata-rata pemakaian listrik harian(wh): ")
tarif_listrik = 1325
wh = float(nilai)

## mengubah wh ke kwh ##
harian= float(wh/1000)
bulanan = float(harian * 30)
harga = float(bulanan * tarif_listrik)

print("jumlah tagihan listrik bulanan : Rp. %.2f" % (harga))