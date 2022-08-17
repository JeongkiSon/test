#maze
'''
BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
모든 노드의 최단 거리 값을 기록하는 방식으로 해결 가능
'''
from collections import deque

n , m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)
# exit()    

# visited = [[False] * n for i in range(m)]

dx = [0, 1]
dy = [1, 0] 
#오른쪽 과 아래로 가는경우

    
def bfs(x, y):  #오른쪽이나 아래가 1이면 enqueue
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()  #원소 뽑으면서 안 갔던 곳&&1인곳에 한해서 거리 업데이트
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0  or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            
            # print(nx, ny)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
           
    
    # print(graph) 
    return graph[n-1][m-1]


print(bfs(0, 0))
