def faktorial(nilai):
    if nilai == 0:
        return 1
    else:
        return nilai*faktorial(nilai-1)

n = int(input(""))

print(faktorial(nilai=n))