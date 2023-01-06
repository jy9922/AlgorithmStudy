import sys
input = sys.stdin.readline

# 카드 놓기
n = int(input())
k = int(input())
card = [0] * n
res = [0] * k
ch = [0] * n

answer = []

for j in range(n):
  a = int(input())
  card[j] = a

# DFS를 이용한 k개 조합
def DFS(L):
  if L == k:
    # 숫자 추출하기
    b = ''.join(res)
    answer.append(b)
    return
  else:
    for i in range(n):
      if ch[i] == 0:
        ch[i] = 1
        res[L] = str(card[i])
        DFS(L+1)
        ch[i] = 0

DFS(0)

# 중복제거 후 개수 출력
print(len(set(answer)))
