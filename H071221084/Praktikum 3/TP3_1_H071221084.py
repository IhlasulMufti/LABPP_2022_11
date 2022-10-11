x = int(input('Masukkan X: '))
y = int(input('Masukkan Y: '))

if x < y:
    for i in range(1, y+1):
        print(i , end = ' \n' if i % x == 0 else ' ')
else:
    print('Invalid')