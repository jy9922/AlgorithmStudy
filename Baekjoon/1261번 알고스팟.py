# 알고스팟
# 항상 같은 방에 있어야 한다.
# 상하좌우로 인접한 방으로만 이동 가능

# 알고스팟 무기가 있다면 벽을 무수어 버릴 수 있다.
# 벽을 부수면, 빈 방과 동일한 방

# (1,1) -> (n,m)
# 최소 몇 번의 벽을 부숴야 하는지

from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
visited[0][0] = 0

while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
      if graph[nx][ny] == 0:
        visited[nx][ny] = visited[x][y]
        q.appendleft((nx, ny))
      else:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))

print(visited[n-1][m-1])
