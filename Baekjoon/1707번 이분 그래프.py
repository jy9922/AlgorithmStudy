# 이분 그래프
# 정점의 집합을 둘로 분할 -> 각 집합에 속한 정점끼리
# 서로 인접하지 않도록 분할 -> 이분 그래프
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

t = int(input())

def dfs(start, color):
  global error

  if error:
    return
  # 방문한 정점 색 칠하기
  visited[start] = color

  # 연결된 노드 찾기
  for i in graph[start]:
    # 연결된 노드 중 방문하지 않은 노드가 있다면
    if not visited[i]:
      # 다른 색 칠하고 호출하기
      dfs(i, -color)
    # 인접한(연결된) 노드값이 현재 노드값과 그룹이 갔다면 False
    elif visited[i] == visited[start]:
      error = True
      return
  

for _ in range(t):
  nv, ne = map(int, input().split())
  graph = [[] for _ in range(nv+1)]
  visited = [False] * (nv+1)
  error = False
  
  for i in range(ne):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  for j in range(1, nv+1):
    if not visited[j]:
      dfs(j, 1)
      # 만약 error가 True 나왔다면 더 이상 수행할 필요 X
      if error:
        break
        
  print("NO" if error else "YES")
