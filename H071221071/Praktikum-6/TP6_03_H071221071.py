namafile = input("Nama File: ") + ".txt"
jumlah = int(input("Jumlah data: "))

f = open(namafile, "w")

try:
    f.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    f.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    f.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")

    for i in range(jumlah):
        nama = input("Masukkan Nama: ").replace(" ","_")
        if len(nama) > 20:
            raise 
        nim = input("Masukkan NIM: ")
        angkatan = input("Angkatan: ")

        f.write("|" + " " + nama + " "*(22 - (len(nama)+1)) + "| " + nim + " | " + angkatan + " "*5 + "|" + "\n")
    f.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")

    print("Berhasil")
except:
    print("Gagal")

f.close()