# 에디터
import sys
input = sys.stdin.readline

stk1 = list(input().rstrip())
n = int(input())
stk2 = []

# 커서를 기준으로 스택을 두개로 나눔
for i in range(n):
  order = input()
  if order[0] == 'L':
    if stk1:
      stk2.append(stk1.pop())
  elif order[0] == 'B':
    if stk1:
      stk1.pop()
  elif order[0] == 'D':
    if stk2:
      stk1.append(stk2.pop())
  else:
    stk1.append(order[2])

stk1.extend(reversed(stk2))
print(''.join(stk1))
  
