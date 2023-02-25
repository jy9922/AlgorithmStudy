# 쉬운 최단거리
from collections import deque

n, m = map(int, input().split())
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      sx, sy = i, j
      distance[i][j] = 0
      visited[i][j] = True
    if graph[i][j] == 0:
      distance[i][j] = 0

q = deque()
q.append((sx, sy))
while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
      distance[nx][ny] = distance[x][y] + 1
      visited[nx][ny] = True
      q.append((nx, ny))
      
for i in range(n):
  for j in range(m):
    print(distance[i][j], end=' ')
  print()
