from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      x, y = i, j
      
size = 2

def bfs(x, y, s):
  dis = [[0] * n for _ in range(n)]
  visited = [[0] * n for _ in range(n)]
  tmp = []
  q = deque()
  q.append((x, y))
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        if graph[nx][ny] <= s:
          visited[nx][ny] = 1
          dis[nx][ny] = dis[x][y] + 1
          q.append((nx, ny))
          if graph[nx][ny] < s and graph[nx][ny] != 0:
            tmp.append((nx, ny, dis[nx][ny]))
          
  return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))

result, cnt = 0, 0
while True:
  shark = bfs(x, y, size)
  
  if len(shark) == 0:
    break
    
  nx, ny, time = shark.pop()
  graph[x][y], graph[nx][ny] = 0, 0
  cnt += 1
  result += time
  x, y = nx, ny
  
  if cnt == size:
    size += 1
    cnt = 0
    
print(result) 
          
      
