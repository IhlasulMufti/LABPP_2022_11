def getFPB(a, b):
    if (b == 0):
        return a
    else:
        return getFPB(b, a % b)
    
angka_1 = int(input(""))
angka_2 = int(input(""))
print(f"FPB ({angka_1}, {angka_2}) = {getFPB(angka_1,angka_2)}")
