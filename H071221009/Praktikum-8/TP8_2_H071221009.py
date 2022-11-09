# membuat sebuah class berdasarkan class diagram

class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = 0.0
        self.massa_jenis = 0.0
    def set_Lebar(self, lebar):
        self.lebar = lebar
    def set_Tinggi(self, tinggi):
        self.tinggi = tinggi
    def set_Panjang(self, panjang):
        self.panjang = panjang
    def setMassa(self, massa):
        self.massa = massa
    def getMassaJenis(self):
        self.massa_jenis = self.massa/(self.panjang*self.lebar*self.tinggi)
        return self.massa_jenis

lebar = float(input("input lebar: "))
tinggi = float(input("input tinggi: "))
panjang = float(input("input panjang: "))
massa = float(input("input massa: "))

kubus = Kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setMassa(massa*2)
kubus.set_Panjang(float(input("input panjang baru: ")))
print("Massa Jenis =", kubus.getMassaJenis())