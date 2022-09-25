## program konversi detik ke dalam jam ##
 
detik = int(input("Masukkan Jumlah Detik yang ingin di hitung : "))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(jam,'jam :',menit,'menit :',detik,'detik')