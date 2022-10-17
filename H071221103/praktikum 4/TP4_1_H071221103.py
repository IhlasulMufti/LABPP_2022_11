def faktorial(nilai) :
    if nilai == 0:
        return 1
    
    else :
        return nilai *  faktorial(nilai - 1)

angka = int(input('bilangan bulat : '))
print(faktorial(angka))