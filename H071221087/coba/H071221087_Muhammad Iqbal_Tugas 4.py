## Kalkulator sederhana ##
print('====================')
print('Kalkulator sederhana')
print('====================')
print(' ')

angka_satu = int(input('Masukkan Angka : '))
option = input('Pilih Opsi ( +, -, *, / ) :')
angka_dua = int(input('Masukkan Angka : '))

opsi_plus = angka_satu + angka_dua
opsi_min = angka_satu - angka_dua
opsi_kali = angka_satu * angka_dua
opsi_bagi = angka_satu / angka_dua
print('--------------------')

if option == '+' :
    print('Hasilnya adalah :' + str(opsi_plus))
elif option == '-' : 
    print('Hasilnya adalah :' + str(opsi_min))
elif option == '*' : 
    print('Hasilnya adalah :' + str(opsi_kali))
elif option == '/' :
    print('Hasilnya adalah :' + str(opsi_bagi))