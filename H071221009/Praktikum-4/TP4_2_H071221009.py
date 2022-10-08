def getFPB(nilai_a, nilai_b):
    if (nilai_b == 0):
        return nilai_a
    else:
        return getFPB(nilai_b, nilai_a % nilai_b)

a = int(input(""))
b = int(input(""))

print(f"FPB ({a}, {b}) = {getFPB(a, b)}")