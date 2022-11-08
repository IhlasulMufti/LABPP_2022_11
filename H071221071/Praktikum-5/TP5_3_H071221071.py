x = list(map(int, input("Masukkan Array 1: ").split()))
y = list(map(int, input("Masukkan Array 2: ").split())) 
x1 = set(x)
y1 = set(y)
print(x1)
n = []
for i in x:
    if i in y:
        n.append(i)

tuple_1 = tuple(x1 & y1)
    
if len(n) == 0:
    print ("tidak ada duplikat")
else:
    print(f"Terdapat {len(x1 & y1)} buah duplikat yaitu {tuple_1}")