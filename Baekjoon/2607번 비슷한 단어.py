# 비슷한 단어
from collections import defaultdict
import copy

n = int(input())
dist = defaultdict(int)

s = input()
for j in s:
  dist[j] += 1

cnt = 0
for _ in range(n-1):
  dist2 = copy.deepcopy(dist)
  ss = input()
  ans = 0
  for i in ss:
    if dist2[i] > 0:
      dist2[i] -= 1
      ans += 1
      
  # 첫번째 문자열 길이가 더 긴 경우, 첫번째 문자열에서 얼만큼 일치하는지 개수 확인
  if len(s) > len(ss):
    if abs(len(s) - ans) < 2:
      cnt += 1
  else:
   # 비교하고자 하는 문자열의 길이가 더 긴 경우, 일치한 문자열 개수 확인
    if len(s) <= len(ss):
      if abs(len(ss) - ans) < 2:
        cnt += 1

print(cnt)
