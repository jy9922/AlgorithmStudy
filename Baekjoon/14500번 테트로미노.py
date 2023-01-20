# 테트로미노
# (ㅏ,ㅗ,ㅓ,ㅜ)를 제외하고 나머지는 4방향으로 움직이면 완성되는 모형이다.
# 따라서 4가지 방향 탐색이 가능한 모형은 DFS를 이용해 탐색하고
# (ㅏ, ㅗ, ㅓ, ㅜ)는 가운데를 중심으로 3방향으로 탐색하는 방법으로 
# 최대값을 구한다.

# 4방향 탐색 방법
def DFS(cnt, x, y, dsum):
  global maxSum
  if cnt == 4:
    maxSum = max(maxSum, dsum)
    return
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
        visited[nx][ny] = True
        DFS(cnt+1, nx, ny, dsum+graph[nx][ny])
        visited[nx][ny] = False
        
# ㅏ, ㅓ, ㅗ, ㅜ를 탐색하는 방법  
def Exec(x, y, dsum):
  global maxSum
  for i in range(4):
    tmp = dsum
    for j in range(3):
      t = (i + j) % 4
      nx = x + dx[t]
      ny = y + dy[t]
      if not (0<=nx<n and 0<=ny<m):
        tmp = 0
        break
      tmp += graph[nx][ny]
    maxSum = max(maxSum, tmp) 
    
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy =[0,0,-1,1]
maxSum = 0

for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      visited[i][j] = True
      DFS(1, i, j, graph[i][j])
      visited[i][j] = False
      Exec(i, j, graph[i][j])

print(maxSum)
