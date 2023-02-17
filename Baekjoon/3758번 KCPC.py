# KCPC
T = int(input())
for _ in range(T):
  n, k, t, m = map(int, input().split())
  board = [[0] * (k+1) for _ in range(n+1)]
  count = [0] * (n+1)
  time = [0] * (n+1)
  for ts in range(m):
    i, j, s = map(int, input().split())
    # 같은 문제 여러번 제출 시 높은 점수가 최종 점수
    board[i][j] = max(board[i][j], s)
    count[i] += 1
    time[i] = ts

  res = [] * n
  for i in range(n+1):
    res.append((sum(board[i]), count[i], time[i], i))
    
  # 점수 총합, 풀이 제출 횟수, 마지막 제출 순으로 정렬
  res.sort(key=lambda x: (-x[0], x[1], x[2]))
  for j in range(len(res)+1):
    x, y, z, a = res[j]
    if a == t:
      print(j+1)
      break
    
  
    
