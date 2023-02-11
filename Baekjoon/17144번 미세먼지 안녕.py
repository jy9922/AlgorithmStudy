r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
  if graph[i][0] == -1:
    gx = i
    gx2 = i+1
    break
      
def spread():
  tmp = [[0] * c for _ in range(r)]
  dx = [-1,0,1,0]
  dy = [0,-1,0,1]
  for i in range(r):
    for j in range(c):
      if graph[i][j] != -1 and graph[i][j] != 0:
        tmp_v = 0
        for d in range(4):
          nx = i + dx[d]
          ny = j + dy[d]
          if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            tmp[nx][ny] += graph[i][j] // 5
            tmp_v += graph[i][j] // 5
        graph[i][j] -= tmp_v
  for i in range(r):
    for j in range(c):
      graph[i][j] += tmp[i][j]

def up():
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]
  x, y = gx, 1
  before, direct = 0, 0
  while True:
    nx = x + dx[direct]
    ny = y + dy[direct]
    if x == gx and y == 0:
      break
    if nx < 0 or nx >= r or ny < 0 or ny >=c:
      direct += 1    
      continue
    graph[x][y], before = before, graph[x][y]
    x, y = nx, ny
    
  
def down():
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  x, y = gx2, 1
  before, direct = 0, 0
  while True:
    nx = x + dx[direct]
    ny = y + dy[direct]
    if x == gx2 and y == 0:
      break
    if nx < 0 or nx >= r or ny < 0 or ny >=c:
      direct += 1
      continue
    graph[x][y], before = before, graph[x][y]
    x, y = nx, ny

for i in range(t):
  spread()
  up()
  down()
  
total = 0
for i in range(r):
  for j in range(c):
    if graph[i][j] > 0:
      total += graph[i][j]

print(total)
