print("mengubah detik ke dalam jam,menit,dan detik")

detik = int(input("Masukkan jumlah detiknya: "))

jam = detik //3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(jam,'jam :',menit,'menit:',detik,'detik:')