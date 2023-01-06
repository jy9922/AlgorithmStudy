# 집합의 표현
# 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지 확인
# 0 a b ( a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합친다는 의미 )
# 1 a b ( a와 b가 같은 집합에 포함되어 있는지 확인)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

# parent 테이블 자기 자신으로 초기화
parent = [i for i in range(n+1)]

# 루트 노드 찾을 때까지 재귀 호출
def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

# 합집합 테이블
def union(x,y):
  x = find(x)
  y = find(y)

  if x < y:
    parent[y] = x
  else:
    parent[x] = y

  
for i in range(m):
  num, a, b = map(int, input().split())
  # 0이면 합집합 호출
  if num == 0:
    union(a, b)
  elif num == 1:
    # a와 b가 같은 집합에 포함되어 있을 때
    if find(a) == find(b):
      print('YES')
    else:
      print('NO')
  
