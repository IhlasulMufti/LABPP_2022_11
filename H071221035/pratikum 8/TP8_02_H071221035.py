class Kubus :
    #
    def __init__(self,lebar,tinggi,panjang) :
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = 0.0
        self.massaJenis = 0.0
    def setMassa (self, massa):
        self.massa = float (massa)
    def setLebar (self, lebar) :
        self.lebar = float (lebar)
    def setPanjang (self, panjang) :
        self.panjang = float (panjang)
    def setTinggi (self, tinggi) :
        self.tinggi = float (tinggi)
    def getMassaJenis (self) :
        return self.massa/(self.lebar*self.tinggi*self.panjang) 
#inputan
lebar = float(input("lebar :"))
tinggi = float(input("tinggi :"))
panjang = float(input("panjang :"))
massa = float(input("massa :"))

#objek
kubus = Kubus (lebar,tinggi,panjang)
#
kubus.setMassa (massa)
print("Massa jenis =", kubus.getMassaJenis())


kubus.setMassa (massa*2)
kubus.setPanjang(20)
kubus.setLebar(15)
print ("Massa jenis =", kubus.getMassaJenis())