def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

n = int(input("masukkan nilai : "))
print (faktorial(n))