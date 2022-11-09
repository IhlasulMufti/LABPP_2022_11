# membuat program sederhana dari class diagram

class Person:
    def __init__(self, name, age, gender, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        if gender == "pria":
            self.isMale = True
            self.gender = "pria"
        elif gender == "wanita":
            self.isMale = False
            self.gender = "wanita"
        else:
            print("Gender salah")

    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_gender(self, gender):
        if gender == "pria":
            self.isMale = True
            self.gender = "pria"
        elif gender == "wanita":
            self.isMale = False
            self.gender = "wanita"
        else:
            print("Gender salah")
    def set_hobby(self, hobby):
        self.hobby = hobby
    def getName(self):
        return self.name
    def getAge(self):
        return self.age 
    def getGender(self):
        return self.gender
    def getHobby(self):
        return self.hobby

name = input("Input nama: ")
age = int(input("Input umur: "))
gender = input("Input jenis kelamin: ")
hobby = input("Input hobi: ")

rumah1 = Person(name, age, gender, hobby)

print(rumah1.getName(), rumah1.getAge(), rumah1.getGender(), rumah1.getHobby())
print(rumah1.isMale)

while True:
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Jenis Kelamin")
    print("5. Ubah Hobi")
    print("6. Keluar")
    
    opsi = input("Input opsi : ")
    try :
        opsi = int(opsi)
    except :
        print("Inputan salah")
    else:
        match opsi:
            case 1:
                print("Data anda adalah")
                print('Nama :', rumah1.getName())
                print('Umur :', rumah1.getAge())
                print('Jenis kelamin :', rumah1.getGender())
                print('Hobi :', rumah1.getHobby())
            case 2:
                rumah1.set_name(input("Input nama baru: "))
                print("Data Anda sukses di perbarui")
            case 3:
                rumah1.set_age(input("Input umur baru: "))
                print("Data Anda sukses di perbarui")
            case 4:
                rumah1.set_gender(input("Input jenis kelamin baru: "))
                print("Data Anda sukses di perbarui")
            case 5:
                rumah1.set_hobby(input("Input hobi baru: "))
                print("Data Anda sukses di perbarui")
            case 6:
                print('Sampai Jumpa', rumah1.getName())
                break