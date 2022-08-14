t = input()

x = int(t[1])
y = ord(t[0]) - ord('a') + 1


dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

cnt = 0
#move to a knight position
for i in range(8):
    if 1<= x+dx[i] <= 8 and 1<= y+dy[i] <= 8:
        cnt += 1
        #print(x+dx[i], y+dy[i])

print(cnt)
