harga = int(input('Harganya : '))
bayar = int(input('Silahkan bayar : '))
kembalian = bayar - harga

if harga < bayar:
    for pecahan in [100000, 50000, 20000, 10000, 5000, 2000, 1000]:
        total_pecahan = (kembalian // pecahan)
        kembalian = kembalian - (pecahan * total_pecahan)
        print('{} uang Rp.{}'.format(total_pecahan, pecahan))
else:
    print("Uangnya kurang")