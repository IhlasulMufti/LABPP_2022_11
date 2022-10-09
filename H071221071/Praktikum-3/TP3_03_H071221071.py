harga = int(input('harga barang: '))
bayar = int(input('nilai uang yang dibayarkan: '))
kembalian = bayar - harga
uang = [100000,50000,20000,10000,5000,1000]

if(bayar<harga):
    print("uang anda kurang")
    exit()
    
for i in (uang):
    bagi = kembalian // i
    kembalian -= bagi * i
    print('%d uang Rp %d'%(bagi,i))
    break
    
