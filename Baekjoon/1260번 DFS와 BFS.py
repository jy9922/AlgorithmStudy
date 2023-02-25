# DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())
arr = [[] * (n+1) for _ in range(n+1)]
for i in range(m):
  s, t = map(int, input().split())
  arr[s].append(t)
  arr[t].append(s)

for j in arr:
  j.sort()

visited = [0] * (n+1)

# DFS
def DFS(L):
  if visited[L] == 1:
    print(L, end=' ')
  for i in arr[L]:
    if visited[i] == 0:
      visited[i] = 1
      DFS(i)

visited[v] = 1
DFS(v)
print()

visited = [0] * (n+1)
q = deque()

def BFS():
  while q:
    x = q.popleft()
    print(x, end=' ')
    for i in arr[x]:
      if visited[i] == 0:
        visited[i] = 1
        q.append(i)

visited[v] = 1
q.append(v)
BFS()
