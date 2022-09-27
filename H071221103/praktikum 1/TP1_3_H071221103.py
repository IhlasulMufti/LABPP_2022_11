print ('program merubah detik ke jam')

detik = int(input('masukkan jumlah detik yang ingin dihitung : '))

jam  = detik // 3600;
sisa_detik = detik % 3600;
menit      = sisa_detik // 60;
detik      = sisa_detik % 60;

print (detik,' detik = ', jam, '  jam, ', menit,' menit,',detik, 'detik')
