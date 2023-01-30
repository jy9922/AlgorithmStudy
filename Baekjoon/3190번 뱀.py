# 뱀
from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]

# 방향(오, 아래, 왼, 위)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

L = int(input())
dir = dict()
q = deque()
q.append((0, 0))

for i in range(L):
    x, d = input().split()
    dir[int(x)] = d

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

# 방향 전환
def Turn(alpha):
  global direction
  if alpha == 'L':
    direction = (direction-1) % 4
  else:
    direction = (direction+1) % 4
    
while True:
  cnt += 1
  x += dx[direction]
  y += dy[direction]

  if x < 0 or x >= n or y < 0 or y >= n:
    break

  if graph[x][y] == 0: # 아무것도 없는 경우
    graph[x][y] = 1
    q.append((x,y)) # 머리 부분 push
    tx, ty = q.popleft() # 꼬리 위치 구하기
    graph[tx][ty] = 0 # 몸통 길이 그대로
    if cnt in dir:
      Turn(dir[cnt])
  elif graph[x][y] == 2: # 사과를 먹었을 경우
    graph[x][y] = 1
    q.append((x, y)) # 머리 부분 push하기 (길이 길어짐)
    if cnt in dir:
      Turn(dir[cnt])
  else:
    break

print(cnt)
