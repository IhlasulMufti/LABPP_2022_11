try:
    a = input('Masukkan nama file : ') + '.txt'
    b = input('Masukkan nama file salinan : ') + '.txt'
    cek_len = 0 
    with open (a, 'r') as file_asli :
        for x in file_asli :
            if len (x) > cek_len :
                cek_len = len(x)
                
    with open (a, 'r') as file_asli :
        r = 1
        s = len(file_asli.readlines())
       
    with open(a, 'r') as file_asli : 
        copy = open(b, 'w')
        for i in file_asli:
            if r<s :
                new_text = f"{i.rstrip():>{cek_len}}\n"
            else :
                new_text = f"{i.rstrip():>{cek_len}}"
            copy.write(new_text)
            r+=1
        copy.close()
    print('\nBerhasil')

except:
    print('\nGagal')
