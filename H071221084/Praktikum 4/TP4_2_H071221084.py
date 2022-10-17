def fpb (a, b):
    if (b == 0):
        return a
    else:
        return fpb (b, a % b)
    
a = int(input(""))
b = int(input(""))
print(f"FPB ({a}, {b}) = {fpb(a,b)}")
