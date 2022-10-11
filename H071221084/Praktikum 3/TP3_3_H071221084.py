a = int(input('Harga barang         : '))
b = int(input('Uang yang dibayarkan : '))

kembalian = b - a

for i in [100000, 50000, 20000, 10000, 5000, 2000, 1000]:
    pecahan = (kembalian//i)
    kembalian -= pecahan*i
    print("{} uang Rp. {}".format(pecahan, i))