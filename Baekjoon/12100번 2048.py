# 2048 게임
# 조건 1) 최대 5번 이동
# 조건 2) 이미 합쳐진 블록은 다시 합쳐지지 않음

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer, q = 0, deque()

# 큐에 삽입
def get(i,j):
  if graph[i][j]:
    q.append(graph[i][j])
    graph[i][j] = 0

# 합치기
def merge(x, y, dx, dy):
  while q:
    a = q.popleft()
    # 그래프의 값이 0이라면
    if graph[x][y] == 0:
      graph[x][y] = a
    # 해당 위치의 값이 같다면 *2
    # 이후 x, y 위치 이동
    elif graph[x][y] == a:
      graph[x][y] = a*2
      x, y = x+dx, y+dy
    # 해당 위치의 값이 다르다면
    else:
      x, y = x+dx, y+dy
      graph[x][y] = a
  
def move(k):
  if k == 0: # 위로 이동, 블럭이 모두 맨 위로 이동
    for j in range(n):
      for i in range(n):
        get(i, j) 
      merge(0, j, 1, 0) # row index를 1씩 증가하며 아래쪽 이동
  elif k == 1: # 아래로 이동, 블럭이 모두 맨 아래로 이동
    for j in range(n):
      for i in range(n-1, -1, -1):
        get(i,j)
      merge(n-1, j, -1, 0) # row index를 1씩 감소하며 위쪽 이동
  elif k == 2: # 왼쪽으로 이동, 블럭이 모두 맨 왼쪽으로로 이동
    for i in range(n):
      for j in range(n):
        get(i, j)
      merge(i, 0, 0, 1) # column index 1씩 증가하며 오른쪽 이동
  else: # 오른쪽 이동, 블럭이 모두 맨 오른쪽으로 이동
    for i in range(n):
      for j in range(n-1, -1, -1):
        get(i, j)
      merge(i, n-1, 0, -1) # column index 1씩 감소하며 왼쪽 이동

def dfs(L):
  global graph, answer
  if L == 5: # 최대 5번 이동
    for i in range(n): 
      answer = max(answer, max(graph[i])) # 가장 큰 값 구하기
    return
  else:
    d = [x[:] for x in graph] # 방향 바꾸기 전 원본 그래프 기억
    for i in range(4): # 4방향으로 움직임
      move(i)
      dfs(L+1)
      graph = [x[:] for x in d]

dfs(0)
print(answer)
    
