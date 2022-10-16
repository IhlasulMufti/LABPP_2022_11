x = int(input('Angka : '))
y = int(input('Angka : '))

if x < y:
    for i in range(1, y + 1):
        print(i, end=" ")    
        if i % x == 0:
            print()
elif x > y:
    print("data tidak valid")