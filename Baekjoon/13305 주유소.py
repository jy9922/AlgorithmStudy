# 주유소
n = int(input())
load = list(map(int, input().split()))
cost = list(map(int, input().split()))

total = 0
m_cost = cost[0]

for i in range(len(cost)-1):
  m_cost = min(m_cost, cost[i])
  total += load[i] * m_cost

print(total)
  
