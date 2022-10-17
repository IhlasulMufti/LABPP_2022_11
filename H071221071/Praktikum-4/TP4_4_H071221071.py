def robot():
    x = 0
    y = 0
    while True:
        s = input().lower()
        if s == 'start':
            x = 0
            y = 0 
            print(x,y)
            continue
        elif s == 'end':
            break
        elif x == 0 and y == 0:
            print(x,y)
        for i in s:
            if i == 'r':
                x += 1
            elif i == 'l':
                x -= 1
            elif i == 'u':
                y += 1   
            elif i == 'd':
                y -= 1
            else:
                continue
            print(x,y)
robot()

