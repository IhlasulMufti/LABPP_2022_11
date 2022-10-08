def myDay(usia):
    tahun = usia//365
    sisahari = usia%365
    bulan = sisahari // 30
    hari = sisahari % 30
    print(f'{tahun} Tahun')
    print(f'{bulan} Bulan')
    print(f'{hari} Hari')
h = int(input(""))

myDay(h)