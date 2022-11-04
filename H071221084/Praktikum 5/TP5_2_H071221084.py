print("\nSelamat datang untuk memulai silahkan input data anda")

nama = input("Input Nama : ") 
umur = int(input("Input Umur : "))
alamat = input("Input Alamat : ")

data_dict = {
"Nama": nama, 
"Umur": umur,
"Alamat": alamat 
}

def profil():
    print("========================================================")
    print('Selamat datang', data_dict['Nama'] ,'silahkan pilih opsi')
    print("========================================================")
profil()

while True :
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("========================================================")
    a= input("Input opsi : ")
    print("========================================================")

    try :
        a = int(a)
    except :
        print("Inputan salah")
    else:
        match a :
            case 1 :
                print("Data anda adalah")
                print('Nama :', data_dict['Nama'])
                print('Umur :', data_dict['Umur'])
                print('Alamat :', data_dict['Alamat'])
                profil()
            case 2 :
                nama_baru = input("Silahkan input nama baru : ")
                data_dict['Nama'] = nama_baru
                print("Data anda sukses di perbarui")
                profil()
            case 3 :
                umur_baru = input("Silahkan input umur baru : ")
                data_dict['Umur'] = umur_baru
                print("Data anda sukses di perbarui")
                profil()
            case 4 :
                alamat_baru = input("Silahkan input alamat baru : ")
                data_dict['Alamat'] = alamat_baru
                print("Data anda sukses di perbarui")
                profil()
            case 5 :
                print('Selamat Tinggal', data_dict['Nama'])
                break 