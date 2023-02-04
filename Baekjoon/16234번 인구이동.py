# 인구 이동
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(a, b):
  q = deque()
  temp = []
  q.append((a, b))
  temp.append((a, b))
  while q:
    a, b = q.popleft()
    for i in range(4):
      na = a + dx[i]
      nb = b + dy[i]
      if 0 <= na < n and 0 <= nb < n and visited[na][nb] == 0:
        if l <= abs(graph[a][b] - graph[na][nb]) <= r:
          visited[na][nb] = 1
          q.append((na, nb))
          temp.append((na, nb))
  return temp
  
result = 0
while True:
  visited = [[0] * n for _ in range(n)]
  flag = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        visited[i][j] = 1
        country = bfs(i, j)
        if len(country) > 1:
          # 인구 이동이 일어날 경우
          flag = 1
          number = sum([graph[x][y] for x, y in country]) // len(country)
          for x, y in country:
            graph[x][y] = number
  # 더이상 인구 이동이 일어나지 않는 경우
  if flag == 0:
    break
  result += 1

print(result)
