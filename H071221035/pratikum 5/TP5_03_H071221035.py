
array1 = []
array2 = []
duplikat =[]

array1 = input('masukkan angka pertama : ').split( )
array2 = input('masukkan angka kedua : ').split( )

for i in array2:
    if i in array1 :
        duplikat.append(i)
        duplikat.sort()

duplikat = tuple(dict.fromkeys(duplikat))
print(f'terdapat {len(duplikat)} Duplikasi {duplikat}')