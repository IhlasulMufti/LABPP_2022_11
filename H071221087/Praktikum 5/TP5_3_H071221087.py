array1 = []
array2 = []
duplikat = []

array1 = (input("Input angka pertama : "))
array2 = (input("Input angka kedua : "))

for i in array2:
    if i in array1:
        duplikat.append(i)
        duplikat.sort()
print(f'Terdapat {len(duplikat)} Duplikat {duplikat}')