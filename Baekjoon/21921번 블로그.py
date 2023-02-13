# 블로그
from collections import deque

n, x = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
total = 0
ans = []

for idx, v in enumerate(arr):
  q.append(v)
  total += v
  if idx < x - 1:
    continue
  ans.append(total)
  total -= q.popleft()

max_ans = max(ans)
if max_ans == 0:
  print('SAD')
else:
  print(max_ans)
  print(ans.count(max_ans))
