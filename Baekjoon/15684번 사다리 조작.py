# 사다리 조작
n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
combi = [] # 후보군

for _ in range(m):
  a, b = map(int, input().split())
  visited[a][b] = True

# 사다리를 놓을 수 있는 위치 후보군에 넣기
for i in range(1, h+1):
  for j in range(1, n):
    if not visited[i][j] and not visited[i][j-1] and not visited[i][j+1]:
      combi.append([i, j])

# i번째 출발이 i번째 도착했는지 확인
def check():
  for i in range(1, n+1):
    now = i
    for j in range(1, h+1):
      if visited[j][now-1]:
        now -= 1
      elif visited[j][now]:
        now += 1
    if now != i:
      return False
  return True

# 사다리를 제한된 수만큼 놓으면서 확인
def dfs(L, idx):
  global answer
  if L >= answer:
    return
    
  # i번째 출발이 i번째 도착이 맞는지 확인  
  if check():
    answer = L
    return
    
  # 사다리를 하나씩 놓으면서 확인
  for i in range(idx, len(combi)):
    x, y = combi[i]
    # 해당 위치에 사다리를 놓을 수 있는지 확인
    if not visited[x][y-1] and not visited[x][y+1]:
      visited[x][y] = True
      dfs(L+1, i+1)
      visited[x][y] = False

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)
