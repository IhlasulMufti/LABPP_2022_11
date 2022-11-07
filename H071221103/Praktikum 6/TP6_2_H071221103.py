try:
    nama_file = input('Masukkan nama file : ') + '.txt'
    salinan = input('Masukkan nama file salinan : ') + '.txt'
    cek_len = 0 
    with open (nama_file, 'r') as file :
        for x in file :
            if len (x) > cek_len :
                cek_len = len(x)

    with open(nama_file, 'r') as file : 
        copy = open(salinan, 'w')
        for i in file:
            new_text = f"{i.rstrip():>{cek_len}}\n"
            copy.write(new_text)
        copy.close()
    print('\nBerhasil')

except:
    print('\nGagal')