# 초 단위로 기록되는 주식가격
# 가격이 떨어지지 않은 기간이 몇 초인지 출력
# 얼마나 유지하느냐를 보는 문제!

# 큐를 이용한 풀이
from collections import deque
def solution(prices):
    answer = []
    
    cnt = len(prices)
    q = deque()

    for i in range(len(prices)):
        q.append((i, prices[i]))
    while q:
        a = q.popleft()
        result = 0
        for j in q:
            # 가격이 떨어지는 구간이 있으면 시점 구한 후 break
            if a[1] > j[1]:
                # 떨어지는 구간 시점 - 내가 있는 시점
                result = j[0] - a[0]
                break 
            else:
                result = j[0] - a[0]
        answer.append(result)
    return answer
  
# 스택을 이용한 풀이 (효율성 ↑)
def solution(prices):
  answer = [0] * len(prices)
  stack = []
    
  for i, price in enumerate(prices):
      # 주식이 하락장이 왔을 때 상승장에 샀던 정보를 pop
      while stack and price < prices[stack[-1]]:
          j = stack.pop()
          # 하락장의 시점에서 pop한 시점을 뺌
          answer[j] = i - j
      # 주식에 해당 인덱스(시점)를 스택에 저장해둠
      stack.append(i)
  # 아직 스택에 있는 정보(끝까지 유지된 가격) pop
  while stack:
      j = stack.pop()
      answer[j] = len(prices) - j - 1
  return answer
    
