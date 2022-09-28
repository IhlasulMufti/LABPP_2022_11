## Tugas Praktikum 2
detik = int(input("masukkan jumlah detik yang ingin dihitung:"))
jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(jam, menit, detik)

