x=int(input('x = '))
y=int(input('y = '))

if(x>y):
    print("y harus lebih besar dari x")
    exit()
    
for i in range (y):
    i += 1  #MULAI DARI 1
    print(i,end=" ")
    if(i%x == 0):
        print('')