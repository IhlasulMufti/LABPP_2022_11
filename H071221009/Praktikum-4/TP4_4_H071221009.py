def robot(x,y):
    while True:
        a=input().upper()
        if a=="END":
            break
        else:
            a=list(a)
        
        for i in a:
            if i=='U':
                y+=1
            elif i=='L':
                x-=1 
            elif i=='R':
                x+=1
            elif i=='D':
                y-=1
            print(f'{x} {y}')
        else:
            continue
robot(0,0)
print('Program Selesai')