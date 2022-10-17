userinput = int(input())
def nilai_faktorial(nilai_n):
    if nilai_n == 0:
        return 1
    else:
        return nilai_n*nilai_faktorial(nilai_n-1)
print(nilai_faktorial(userinput))