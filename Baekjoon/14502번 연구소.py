from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  tmp = copy.deepcopy(board)

  # 바이러스 부분 큐에 삽입
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 2:
        q.append((i, j))

  # 바이러스 퍼지기
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
        tmp[nx][ny] = 2
        q.append((nx, ny))
        
  # 안전지대 개수 세기
  global answer
  cnt = 0
  
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 0:
        cnt += 1

  answer = max(answer, cnt)

# 벽 세우기 (백트래킹)
def makeWall(cnt):
  if cnt == 3:
    bfs()
    return
  else:
    for i in range(n):
      for j in range(m):
        if board[i][j] == 0:
          board[i][j] = 1
          makeWall(cnt+1)
          board[i][j] = 0
      
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
makeWall(0)
print(answer)

