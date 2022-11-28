# Membuat sebuah class yang menerapkan konsep encapsulation, class abstract, inheritance, dan polymorphis

from abc import ABC, abstractmethod
class MakhlukHidup(ABC):
    @abstractmethod
    def makan(self):
        pass
class Human(MakhlukHidup):
    def __init__ (self, name, umur, nim):
        self.name = name
        self.__umur = umur
        self._nim = nim
    def setUmur(self, umur):
        self.__umur = umur
    def getUmur(self):
        print(self.__umur)
    def setNim(self, nim):
        self._nim = nim
    def getNim(self):
        print(self._nim)
    def makan(self):
        print("Ayo Makan Durian")
class Burung:
    def __init__(self, jenis):
        self._jenis = jenis
    def jalan(self):
        print("Burung sedang berjalan dengan slayy")
class Angsa(Burung):
    def __init__(self, jenis):
        super().__init__(jenis)
    def jalan(self):
        print("Angsa sedang berjalan ke arah kolam")

def jalan(burung):
        burung.jalan()

name = print("Nama : Jennie")
umur = print("Umur : 20")
nim = print("Nim : H071221000")

data = Human(name, umur, nim)

bird = Burung("beo")
run = Angsa("angsa")

jalan(bird)
jalan(run)