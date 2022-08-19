#연결 요소 찾기 connected component
'''
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0: #방문 안됐으면
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y -1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    
    return False



n , m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(result) 

'''
    



n , m = map(int, input().split())



graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]


def dfs(x, y):
    #print(x, y)
    if x < 0 or y <0 or x >= n or y >= m:
        return 0
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])   # 0으로 되어 있던 곳을 모두 방문하면서
                                        # 방문처리(1로 만들고) 하고 그 block 에 대해 result 값 하나 추가
        return 1 #block 아이스크림 만든 경우 인접한 곳 다 1로만듬
    
    else: return 0

# 범위를 벗어나거나  방문처리된 곳이면 0 리턴

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            result += 1

print(result)








