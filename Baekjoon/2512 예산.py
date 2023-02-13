# 예산
n = int(input())
arr = list(map(int, input().split()))
total = int(input())

ans = 0
arr.sort()

# 이분 탐색을 통한 상한선 찾기
left = 0
right = max(arr)
  
while left <= right:
  mid = (left+right) // 2
  sum = 0
  for i in arr:
    if i >= mid:
      sum += mid
    else:
      sum += i
  if sum <= total:
    ans = mid
    left = mid + 1
  else:
    right = mid - 1

print(ans)
