print(40*"=")
print ('menghitung jumlah tagihan listrik berbagai golongan')
print(40*"=")

Golongan = input("Masukkan Golongan listrik :").upper() 
Daya = int(input("Masukkan Daya anda :")) 
Pemakaian = int(input("Masukkan Pemakaian anda dalam sebulan:")) 
if Golongan == "R1" :
    if Daya == 900 :
        Tarif = 1352
    elif Daya == 1300 and Daya == 2200 :
        Tarif = 1444.70
elif Golongan == "R2" :
    if Daya >= 3500 and Daya <= 5500 :
        Tarif = 1699.53
elif Golongan == "R3" :
    if Daya >= 6600 :
        Tarif = 1699.53
elif Golongan == "B2" :
    if Daya >= 6600 and Daya <= 200000 : 
        Tarif = 1444.70
elif Golongan == "B3" :
    if Daya >= 200000 :        
        Tarif = 1114.74
elif Golongan == "I3" :
    if Daya >= 200000 :
        Tarif = 1314.12
elif Golongan == "P1" :
    if Daya >= 6600 and Daya <= 200000 :
        Tarif = 1523.28
else :
    print("data tidak valid")


Tagihan = f"> Jumlah Tagihan Anda : {round(Tarif * Pemakaian,2):_}".replace("_",".")
 #round digunakan untuk membatasi jumlah angka dibelakang koma, replace untuk mngubah atau mengganti sinmbol
x = Tagihan.rfind(".") 
#rfind digunakan untuk menemukan simbol pada progrram
rep = Tagihan[:x]+','+Tagihan[x+1:] #untuk kasi
#rep = replication untuk menggabungkan indeks indeks yang telah diubah , ind = indeks, [:ind]+ untuk menunjukkan simbol kesekian yang akan diubah, [ind+1] untuk menampilkan angka kesatu setelah koma
print(rep)

print(40*"=")
print("Terima Kasih")
print(40*"=")