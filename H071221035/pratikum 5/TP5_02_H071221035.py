
def intro(datadiri):
    print("=" * 25)
    print('Selamat datang', datadiri.get('Nama') ,'silahkan pilih opsi')
    print("=" * 25)

print('='*25 )
print ('selamat datang untuk memulai masukkan data diri anda')
print('='*25 )

nama = input('masukkan nama anda: ')
umur = int(input('masukkan umur anda: '))
alamat = input('masukkan alamat anda: ')

datadiri_dict = {
"Nama": nama, 
"Umur": umur,
"Alamat": alamat 
}

intro(datadiri=datadiri_dict)

while True:
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("=" * 30)
    pilihan = input("Masukkan pilihan anda(1/2/3/4/5) : ")
    print("=" * 30)

    if pilihan == "1" :
        print("=" * 30)
        print("Data anda adalah:")
        print('Nama :',datadiri_dict.get('Nama'))
        print('Umur :',datadiri_dict.get('Umur'))
        print('Alamat :',datadiri_dict.get('Alamat'))
        intro(datadiri=datadiri_dict)
    elif pilihan == "2":
        new_nama = input('masukkan nama baru anda: ')
        datadiri_dict['Nama'] = new_nama
        print ('data anda sukses diperbarui')
        intro(datadiri_dict)
    elif pilihan == "3" :
        new_umur = int(input('masukkan umur baru anda: '))
        datadiri_dict['Umur'] = new_umur
        print ('data anda sukses diperbarui')
        intro(datadiri_dict)
    elif pilihan == "4" :
        new_alamat = input('masukkan alamat baru anda: ')
        datadiri_dict['Alamat'] = new_alamat 
        print('data anda sukses diperbarui')
        intro(datadiri_dict)
    else: 
        print('selamat tinggal',datadiri_dict['Nama'])
        break