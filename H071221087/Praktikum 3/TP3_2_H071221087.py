while True:
    derajat = (input("Masukkan Angka (0 - 360 derajat): "))
    if derajat == "end":
        break
    else:
        hitung = (float (derajat)/15)
        jumlah = int((hitung * 3600) + 21600)

        jam = (jumlah // 3600)
        menit = ((jumlah % 3600) // 60)
        detik = ((jumlah % 3600) % 60)

        if jam > 24:
                jam = jam - 24

        if jam >= 6 and jam < 12:
                print("Selamat Pagi")
        elif jam >= 12 and jam < 16:
                print("Selamat Siang")
        elif jam >= 16 and jam < 19:
                print("Selamat Sore")
        else:
                print("Selamat Malam")

        print(f"{jam:02d}:{menit:02d}:{detik:02d}")