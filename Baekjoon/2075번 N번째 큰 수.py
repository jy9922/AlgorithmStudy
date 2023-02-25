# N번째 큰 수
import heapq

n = int(input())
q = []

for i in range(n):
  arr = list(map(int, input().split()))
  if not q:
    for a in arr:
      heapq.heappush(q, a)
  else:
    for a in arr:
      if q[0] < a:
        heapq.heappush(q, a)
        heapq.heappop(q)
print(q[0])
  
  
