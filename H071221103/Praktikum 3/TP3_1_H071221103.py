print ('program mencetak angka secara vertikal dan horizontal')

x = int(input('masukkan angka x = '))
y = int(input('masukkan angka y = '))

if x > y:
        print ('nilai tidak valid')
else :

        for i in range(1,y+1) :
                print (i, end=' ')
                if i % x == 0 :
                        print()

