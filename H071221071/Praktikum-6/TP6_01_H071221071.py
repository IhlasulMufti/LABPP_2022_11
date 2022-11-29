file1 = input()
file2 = input()

try:
    file_awal = open(f"{file1}.txt","r")
    isi = file_awal.read()

    file_salinan = open(f"{file2}.txt","w")
    file_salinan.write(isi)
    print("Berhasil")
except:
    print('Gagal')

file_awal.close()
file_salinan.close()

