import sys
input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
  a = list(input().split())
  res.append(a)

# 나이순 기준 정렬
res.sort(key=lambda x:int(x[0]))

for age, name in res:
  print(age, name)
