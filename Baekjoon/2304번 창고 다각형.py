# 창고 다각형
n = int(input())
ans = 0

nc = [[0, 0] for _ in range(1001)]
max_x, max_h = 0, 0
for i in range(n):
  x, h = map(int, input().split())
  max_x = max(max_x, x)
  max_h = max(max_h, h)
  nc[x] = [x, h]

max_idx = 0
max_ch = 0

for i in range(1, max_x+1):
  if nc[i][0] != 0:
    if nc[i][1] == max_h:
      max_idx = i

# 왼쪽부터 탐색
for j in range(1, max_idx):
  max_ch = max(max_ch, nc[j][1])
  ans += max_ch

max_ch = 0
for k in range(max_x, max_idx, -1):
  max_ch = max(max_ch, nc[k][1])
  ans += max_ch

print(ans + max_h)
