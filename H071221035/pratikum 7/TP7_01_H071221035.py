import re
#menggunakan try except untuk program yang eror dijadikan false
try:
    #membuat input untuk string
    string_s = input("masukkan String S: ")
    #membuat pola atau syarat kondisi string
    pattern = re.fullmatch("[2468a-zA-Z\-]{40}[13579\s]{5}", string_s)
     #re.fullmatch untuk mengembalikan persamaan pola kalau lebih atau kurang akan false
     #membuat perkondisian untuk menghasilkan berhasil atau gagal
    if pattern :
        print("True S")
    else:
        print("False S")
except:
    print("False")
