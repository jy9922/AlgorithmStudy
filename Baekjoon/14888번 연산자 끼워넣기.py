# 연산자 끼워넣기
# +, -, *, //
# 최대 최소
n = int(input())
m = list(map(int, input().split()))
y = list(map(int, input().split()))
res = []

def DFS(L, sum, pre):
  if L == n:
    res.append(sum)
  else:
    for i in range(4):
      if y[i] == 0:
        continue
      else:
        pre = sum
        if i == 0:
          sum += m[L]
        elif i == 1:
          sum -= m[L]
        elif i == 2:
          sum *= m[L]
        else:
          if sum < 0:
            sum *= -1
            sum //= m[L]
            sum *= -1
          else:
            sum //= m[L]
        y[i] -= 1
        DFS(L+1, sum, pre)
        y[i] += 1
        sum = pre

DFS(1, m[0], m[0])
print(max(res))
print(min(res))
