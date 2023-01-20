# 경사로
# 구현문제
# 현재값과 이전값이 1이상 차이 나는지 확인
# 현재값 < 이전값인 경우 현재값을 기준으로 오른쪽 확인
## 범위를 넘어섰는지 확인
## 현재값과 L만큼 더한 값이 같은지 확인
## 현재값과 L만큼 더한 값이 사용중인지 확인
# 현재값 > 이전값인 경우 이전값을 기준으로 왼쪽 확인

def ladder(now):
  for i in range(1, n):
    if abs(now[i] - now[i-1]) > 1:
      return False
    # 현재값이 이전값보다 작다면, 오른쪽 확인
    if now[i] < now[i-1]:
      for l in range(L):
        if i + l >= n or now[i] != now[i+l] or used[i+l]:
          return False
        if now[i] == now[i+l]:
          used[i+l] = True
    # 현재값이 이전값보다 크다면, 왼쪽 확인
    if now[i] > now[i-1]:
      for l in range(L):
        if i-l-1 < 0 or now[i-1] != now[i-l-1] or used[i-l-1]:
          return False
        if now[i-1] == now[i-l-1]:
          used[i-l-1] = True
  return True

n, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 가로 확인
for i in range(n):
  used = [False for _ in range(n)]
  if ladder(graph[i]):
    result += 1

# 세로 확인
for i in range(n):
  used = [False for _ in range(n)]
  if ladder([graph[j][i] for j in range(n)]):
    result += 1
print(result)
