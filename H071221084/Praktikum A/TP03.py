print ("--- Program Menghitung Volume dan Luas Kerucut ---")

tinggi =float(input("Masukan tinggi         : "))
jari   =float(input("Masukan jari-jari alas : "))

phi = 22/7
pelukis = (jari*jari)+(tinggi*tinggi)

volume = round(1/3*(phi*jari*jari*tinggi),2)
luas = round(phi*jari*jari+(pelukis),2)

print('Volume : ',volume)
print('luas   : ',luas)