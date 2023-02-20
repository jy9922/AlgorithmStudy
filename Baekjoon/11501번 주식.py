# 주식
import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
  day = int(input())
  z = list(map(int, input().split()))

  mz = 0
  v = 0
  
  # 뒤에서 부터 접근해서 max 구하기
  for i in range(len(z)-1, -1, -1):
    if mz <= z[i]:
      mz = z[i]
    else:
      v += mz - z[i]
      
  res.append(v)

for i in res:
  print(i)
    
