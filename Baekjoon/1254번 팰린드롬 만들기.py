# 팰린드롬 만들기
s = input()

# 확장하며 모든 문자열이 펠린드롬 형태로 만들기
def expand(left, right):
  while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1
  if right == len(s):
    return left + 1
  return int(1e9)
  
# 예외
if s == s[::-1]:
  print(len(s))
else: 
  result = int(1e9)
  for i in range(len(s)-1):
    result = min(result, expand(i, i+1), expand(i, i+2))
  print(len(s)+result)
    
    
