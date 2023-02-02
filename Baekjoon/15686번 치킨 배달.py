import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
answer = []
res = [0] * m


# 집 위치 리스트
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house.append((i, j))
    elif graph[i][j] == 2:
      chicken.append((i, j))

visited = [0] * len(chicken)

def DFS(L, t):
  global answer
  if L == m:
    total = 0
    for i in range(len(house)):
      dis = int(1e9)
      for j in range(m):
        a = abs(house[i][0]-res[j][0]) + abs(house[i][1]-res[j][1])
        dis = min(dis, a)
      total += dis
    answer.append(total)
  else:    
    for j in range(t, len(chicken)):
      if visited[j] == 0:
        visited[j] = 1
        res[L] = chicken[j]
        DFS(L+1, j+1)
        visited[j] = 0
    

DFS(0, 0)
print(min(answer))
