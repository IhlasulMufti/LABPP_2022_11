print ('program menghitung kembalian dari suatu transaksi')

harga =int(input('harga barang = '))
jumlah =int(input('nilai uang yang dibayarkan = '))


if harga < jumlah:
    kembalian = jumlah-harga

    n = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    for i in n:
        pembagian_kembalian = kembalian//i
        print(f'{int(pembagian_kembalian)} uang Rp. {i}')
        kembalian = kembalian-(pembagian_kembalian*i)
else :
    print ('uang yang diberikan kurang')
