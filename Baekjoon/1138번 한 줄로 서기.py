# 한 줄로 서기
n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

for k, num in enumerate(arr):
  if answer[num] == 0 and answer[:num].count(0) == num:
    answer[num] = k+1
  else:
    x = num
    while x < n:
      if answer[x] == 0 and answer[:x].count(0) == num:
        answer[x] = k+1
        break
      x += 1
      
for j in answer:
  print(j, end=' ')
