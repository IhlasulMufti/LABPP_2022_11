a = int(input('bilangan 1 : '))
b = int(input('bilangan 2 : '))

def getFPB(a,b):
    if (b == 0):
        return a
    else:
        return getFPB(b, a % b)

print(f'FPB({a},{b}) = ', getFPB(a,b))