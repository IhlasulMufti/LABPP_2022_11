x = y = 0

def robot():
    global x, y, string
    for i in string:
        if i == 'R' :
            X= x+1
        elif i == 'L' :
            x= x-1
        elif i == 'U' :
            y= y+1
        elif i == 'D' :
            y= y-1
        else :
            continue
        print(x,y)

string = input().upper()
print(x,y)
robot()

while True :
    string = input().upper()
    if string == 'END' :
        break
    elif string == "START" :
        x = 0
        y = 0
    else :
        robot()