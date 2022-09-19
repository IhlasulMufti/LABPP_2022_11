#PRATIKUM 01 SOAL NO 2
#program merubah detik menjadi ke dalam format jam:menit:detik

# 1 menit = 60 detik
# 1 jam   = 60 menit

detik = int(input ("masukkan nilai detik:"))
menit = detik // 60
jam = menit // 60

print ("%02d:%02d:%02d"% (jam, menit % 60, detik % 60))
