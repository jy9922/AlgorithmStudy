from collections import deque

n, m, K = map(int, input().split())
# 처음에는 양분이 5로 세팅
ground = [[5] * n for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 겨울마다 추가 되는 양분
winter = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

while K > 0:
  # 봄
  for i in range(n):
    for j in range(n):
      t_len = len(tree[i][j])
      for k in range(t_len):
        if ground[i][j] >= tree[i][j][k]:
          ground[i][j] -= tree[i][j][k]
          tree[i][j][k] += 1
        else:
          # 여름
          for _ in range(k, t_len):
            ground[i][j] += tree[i][j].pop() // 2
          break

  # 가을
  for i in range(n):
    for j in range(n):
      for z in tree[i][j]:
        if z % 5 == 0:
          for d in range(8):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
              tree[nx][ny].appendleft(1)
      # 겨울
      ground[i][j] += winter[i][j]
  K -= 1
  
result = 0
for i in range(n):
  for j in range(n):
    result += len(tree[i][j])

print(result)
