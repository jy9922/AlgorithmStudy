# 가희와 키워드
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
kl = defaultdict(int)

for i in range(n):
  k = input().rstrip()
  kl[k] += 1

answer = n
for i in range(m):
  a = input().rstrip().split(',')
  for j in a:
    if j in kl.keys() and kl[j] == 1:
      kl[j] -= 1
      answer -= 1
  print(answer)
