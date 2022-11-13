filename = input() + ".txt"
n = int(input())

a = open(filename, "w+")
try:
    for i in range(n):
        nama = input().replace(' ', '_')
        nim = input()
        angkatan = input()    
    
    a.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    a.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    a.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    a.write("|" + " " + nama + " "*(22 - (len(nama)+1)) + "| " + nim + " | " + angkatan + " "*5 + "|" + "\n")
    a.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")
    

    print("Berhasil")
except:
    print("Gagal")
    
a.close()