# IF문 좀 대신 써줘
# 이진 탐색
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rank = [input().split() for _ in range(n)]

def ds(rank, power):
  start, end = 0, len(rank)-1
  res = 0
  while start <= end:
    mid = (start+end)//2
    if int(rank[mid][1]) >= power:
      end = mid - 1
      res = mid
    else:
      start = mid + 1
  return res

for i in range(m):
  pp = int(input())
  print(rank[ds(rank, pp)][0])
