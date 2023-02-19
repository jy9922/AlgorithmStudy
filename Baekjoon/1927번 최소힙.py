# 최소힙
import heapq
import sys
input = sys.stdin.readline

q = []
res = []

n = int(input())
for i in range(n):
  x = int(input().rstrip())
  if x == 0:
    if q:
      t = heapq.heappop(q)
      res.append(t)
    else:
      res.append(0)
  else:
    heapq.heappush(q, x)
for j in res:
  print(j)
