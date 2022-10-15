x=y=0
def robot() :
    global x 
    global y
    for i in string:
        if i== "R" :
            x+=1
            # print(x,y)
        elif i== "L" :
            x-=1
            # print(x,y)
        elif i=="U":
            y+=1
            # print(x,y)
        elif i== "D":
            y-=1
            # print(x,y)
        else:
            continue
        print (x,y)
    return x,y

print(x,y)
# robot(x,y)

while True:
    string= input().upper()
    if string== "END" :
        break
    elif string == "START" :
        x=0
        y=0
        print (x,y)
    else :
        robot()
