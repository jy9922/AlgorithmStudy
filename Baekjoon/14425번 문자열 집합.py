# 문자열 집합
from collections import defaultdict

n, m = map(int, input().split())
dic = defaultdict(int)

for i in range(n):
  a = input()
  dic[a] += 1

count = 0
for j in range(m):
  b = input()
  if dic[b] > 0:
    count += 1

print(count)
  
