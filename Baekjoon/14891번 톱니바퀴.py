# 톱니바퀴
# 톱니바퀴 하나만 돌려도 전체에 영향을 미치므로 DFS 사용
# 시계 방향으로 도는 함수, 반시계 방향으로 도는 함수

graph = [list(map(int, input())) for _ in range(4)]
k = int(input())

# 시계방향 함수
def rotate_clock(graph):
  tmp = graph[7]
  for i in range(6, -1, -1):
    graph[i+1] = graph[i]
  graph[0] = tmp
# 반시계방향 함수
def ban_rotate_graph(graph):
  tmp = graph[0]
  for i in range(7):
    graph[i] = graph[i+1]
  graph[7] = tmp
# 톱니바퀴 하나 굴렸을 때 DFS 호출
def dfs(x, d):
  global visited
  if visited[x] == 0:
    visited[x] = 1
    left = graph[x][6]
    right = graph[x][2]
    if d == -1:
      ban_rotate_graph(graph[x])
    else:
      rotate_clock(graph[x])
    if x-1 >= 0 and left != graph[x-1][2]:
      dfs(x-1, -d)
    if x+1 <= 3 and right != graph[x+1][6]:
      dfs(x+1, -d)

for i in range(k):
  x, d = map(int, input().split())
  visited = [0] * 4
  dfs(x-1, d)

answer = 0
for j in range(4):
  if graph[j][0] == 1:
    answer += (2**j)

print(answer)
