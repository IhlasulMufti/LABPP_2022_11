#merubah jumlah hari ke usia
def myday(jumlahhari):
    if jumlahhari >= 0 :
        tahun = jumlahhari // 365
        x = jumlahhari % 365 #untuk menghitung sisa dari variabel tahun
        bulan = x // 30
        hari =  x % 30
        print(f"{tahun} tahun")
        print (f"{bulan} bulan")
        print (f"{hari} hari")
    else :
        print('inputan salah')
jumlahhari = int(input('masukkan jumlah hari: '))

myday(jumlahhari)