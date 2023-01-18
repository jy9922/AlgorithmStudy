# 스티커
# 스티커 2n개 구매
# 2행 n열로 배치
# 스티커 한장을 떼면 스티커 변을 공유하는 스티커는 모두 찢어짐
# 스티커에 점수를 매기고
# 점수의 합이 최대가 되게 스티커를 떼려고함

# 점수의 합이 최대
# 서로 변을 공유하지 않는 스티커 집합

t = int(input())

for i in range(t):
  n = int(input())
  
  s = [list(map(int, input().split())) for _ in range(2)]

  for j in range(1, n):
    if j == 1:
      s[0][j] += s[1][j-1]
      s[1][j] += s[0][j-1]
    else:
      s[0][j] += max(s[1][j-1], s[1][j-2])
      s[1][j] += max(s[0][j-1], s[0][j-2])
      
  print(max(s[0][n-1],s[1][n-1]))
  
