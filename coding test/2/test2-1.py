a = int(input())
dirr = list(input().split())

dx = [0, -1 , 0 ,1 ]
dy = [1, 0, -1, 0]

x , y = 1, 1

#나갔는지 판별
i = -1
for box in dirr:
    if box == 'R':
        i = 0
    elif box == 'U':
        i = 1
    elif box == 'L':
        i = 2
    else: i = 3

    #print("i :", i )
    
    if (x + dx[i]<1 or x + dx[i]>5) or (y + dy[i]<1 or y + dy[i]>5):
        pass
    else: x , y = x + dx[i], y + dy[i]
    
    
print(x, y)
