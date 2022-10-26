print("Selamat Datang, Untuk memulai silahkan input data anda")
nama = input("Masukkan Nama Anda : ")
umur = int(input("MAsukkan Umur Anda : "))
alamat = input("Masukkan Alamat Anda: ")
print(40 * "=")

print("Selamat Datang", nama, "Silahkan pilih opsi")
print(40 * "=")

def menu():
    print("1. Detail Info Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

data = {
    "Nama" : nama,
    "Umur" : umur,
    "Alamat" : alamat
}

menu()
print(40 * "=")
pilihan = input("Pilih Opsi : ")
print(40 * "=")
while pilihan != "5":
    if pilihan == "1":
        print("Data anda adalah ")
        print(40 * "=")
        for key, value in data.items():
                print(f'{key} : {value}')
        print(40 * "=")
    elif pilihan == "2":
            print(40 * "=")
            ubah_nama = input("Masukkan nama yang baru : ")
            data['Nama'] = ubah_nama
            print(40 * "=")
            print("Pengubahan Nama Berhasil")
            print(40 * "=")
    elif pilihan == '3':
            print(40 * "=")
            ubah_umur = input('Input Umur Yang Baru : ')
            data['Umur'] = ubah_umur
            print(40 * "=")
            print('Ubah Umur Berhasil')
            print(40 * "=")
    elif pilihan == '4':
            print(40 * "=")
            ubah_alamat = input('Input Alamat Yang Baru : ')
            data['Alamat'] = ubah_alamat
            print(40 * "=")
            print('Ubah Alamat Berhasil')
            print(40 * "=")
    else:
            print('Error !!!')
    menu()
    print(40 * "=")
    pilihan = input('Pilih Opsi : ')                
print(40 * "=")
print('Selamat Tinggal', data["Nama"] )
    