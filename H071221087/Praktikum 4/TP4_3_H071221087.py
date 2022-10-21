def myDay(day):
    tahun = day//365
    sisahari = day%365
    bulan = sisahari // 30
    hari = sisahari % 30
    print(f'{tahun} Tahun')
    print(f'{bulan} Bulan')
    print(f'{hari} Hari')
    
hari = int(input(""))
myDay(hari)