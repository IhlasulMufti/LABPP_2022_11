watt = input('Total Konsumsi Daya listrik :')
kwh = (int(watt) / 1000*1352*30//1)
print('Jumlah Tagihan Listrik dalam Satu bulan : Rp', kwh)