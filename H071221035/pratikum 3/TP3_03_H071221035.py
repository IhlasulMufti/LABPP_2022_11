#
pembayaran = int(input("masukkan jumlah pembayaran : " ))
harga_barang = int(input("masukkan harga barang : " ))

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]
kembalian = pembayaran - harga_barang

for pecahan in pecahan_uang :
    if kembalian < pecahan :
        continue
    jumlahpecahan =int(kembalian / pecahan)
    kembalian = kembalian -(pecahan * jumlahpecahan)
    print(jumlahpecahan, 'uang Rp', (pecahan))