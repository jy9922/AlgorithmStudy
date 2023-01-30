# 감시
import copy

n, m = map(int, input().split())
graph = []
# cctv 종류 및 위치 정보 저장
cctv = []
# cctv의 방향 모드
mode = [
  [],
  [[0], [1], [2], [3]],
  [[0, 2], [1, 3]],
  [[0, 1], [1, 2], [2, 3], [0, 3]],
  [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
  [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
      
for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  for j in range(m):
    # cctv가 있다면 cctv 리스트에 종류 및 위치 저장
    if data[j] in [1, 2, 3, 4, 5]:
      cctv.append([data[j], i, j])

# 방향이 정해지면 그 방향으로 채우기
def fill(graph, mm, x, y):
  for i in mm:
    # 새로운 변수에 담아주기
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        break
      if graph[nx][ny] == 6:
        break
      elif graph[nx][ny] == 0:
        graph[nx][ny] = 7

# 모든 방향 재귀 호출 -> 만약 탐색이 완료 되었으면 사각지대 개수 카운트
def DFS(L, arr):
  global min_value
  
  if L == len(cctv):
    count = 0
    # 사각지대 갯수 카운트
    for i in range(n):
      count += arr[i].count(0)
    min_value = min(min_value, count)
    return
    
  # graph 깊은 복사 새로운 리스트 생성
  tmp = copy.deepcopy(arr)
  # graph 안에 있는 cctv 정보 확인
  cctv_kind, x, y = cctv[L]
  
  # cctv 종류에 따라 모든 방향 확인하기
  for i in mode[cctv_kind]:
    fill(tmp, i, x, y)
    DFS(L+1, tmp)
    tmp = copy.deepcopy(arr)

min_value = int(1e9)
DFS(0, graph)
print(min_value)
