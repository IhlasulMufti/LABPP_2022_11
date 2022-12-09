class Person:
    negara = "indonesia"
    #self mengacu kepada diri objek
    def __init__(self, name, age, isMale, tinggi):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.tinggi = tinggi
        
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setGender(self, isMale):
        self.isMale = isMale
    def getGender(self):
        if self.isMale == True:
            return ("Male")
        elif self.isMale == False:
            return ("Female")
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def getTinggi(self):
        return self.tinggi
    
#objek
orang1 = Person("Iqbal", 18, True, 166)
orang2 = Person("Izzah", 14, False, 158)

# print(Orang1.__dict__)
orang1.setName("Iqbal")
orang1.setAge(18)
orang1.setGender(True)
orang1.setTinggi(166)
print(orang1.getName(),orang1.getAge(),orang1.getGender(),orang1.getTinggi())

# print(Orang2.__dict__)
orang1.setName("Izzah")
orang1.setAge(14)
orang1.setGender(False)
orang1.setTinggi(158)
print(orang1.getName(),orang1.getAge(),orang1.getGender(),orang1.getTinggi())
