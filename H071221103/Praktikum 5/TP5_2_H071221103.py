def profil():
    print("=" * 70)
    print('Selamat datang', file_dict.get('Nama') ,'silahkan pilih opsi')
    print("=" * 70)

print("=" * 70)
print("Selamat datang untuk memulai silahkan input data anda")
print("=" * 70)

nama = input("Input Nama Anda : ")
umur = int(input("Input Umur Anda : "))
alamat = input("Input Alamat Anda : ")

file_dict = {
"Nama": nama, 
"Umur": umur,
"Alamat": alamat 
}

profil()

while True:
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("=" * 70)
    opsi = int(input('input opsi :'))
    if opsi == 1 :
        print ('='*70)
        print ('data anda adalah \nNama : {} \nUmur : {} \nAlamat : {}'. format(file_dict['Nama'], file_dict['Umur'], file_dict['Alamat']))
    elif opsi == 2 :
        ubah_nama = input('silahkan input Nama baru :')
        file_dict['Nama'] = ubah_nama
        print('data berhasil diperbarui')
    elif opsi == 3 :
        ubah_umur = int(input('silahkan input Umur baru :'))
        file_dict['Umur'] = ubah_umur
        print('data berhasil diperbarui')
    elif opsi == 4 :
        ubah_alamat = input('silahkan input Alamat baru :')
        file_dict['Alamat'] = ubah_alamat
        print('data berhasil diperbarui')
    elif opsi == 5 :
        print ('='*70)
        print ('selamat tinggal', file_dict.get('Nama'))
        break
        
