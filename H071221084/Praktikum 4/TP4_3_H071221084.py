def myDay(hari):
    tahun = hari//365
    sisahari = hari%365
    bulan = sisahari // 30
    hari = sisahari % 30
    print(tahun,'Tahun')
    print(bulan,'Bulan')
    print(hari,'Hari')
    
hari = int(input(""))
myDay(hari)