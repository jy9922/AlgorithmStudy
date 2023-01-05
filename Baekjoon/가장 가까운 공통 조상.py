# 가장 가까운 공통 조상
# 트리 상에서 두 정점이 주어질 때 그들의 가장 가까운 공통 조상은
# 두 노드의 가장 가까운 공통 조상은, 두 노드를 모두 자손으로 가지면서
# 깊이가 가장 깊은(두 노드와 가장 가까운) 노드

# 테스트 케이스 개수 T
# 트리를 구성하는 노드 수
# 간선 정보 (A, B) => A가 B의 부모
# 공통 조상 구할 노드 수

t = int(input())
for _ in range(t):
  n = int(input())
  s = [0] * (n+1)
  for i in range(n-1):
    a, b = map(int, input().split())
    s[b] = a
  na, nb = map(int, input().split())

  # 노드의 부모노드 저장 리스트
  parent = []

  # na 노드를 부모 리스트에 루트 노드까지 저장
  while True :
    if s[na] == 0:
      parent.append(na)
      break
    parent.append(na)
    na = s[na]

  # nb 노드를 부모 리스트에 루트 노드까지 저장하면서
  # parent 리스트에 해당 노드가 있으면 break
  while True:
    if nb in parent:
      print(nb)
      break
    nb = s[nb]
