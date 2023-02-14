# 수 이어 쓰기

n = input()
i = 0
while True:
  i += 1
  nn = str(i)
  while len(nn) > 0 and len(n) > 0:
    if nn[0] == n[0]:
      n = n[1:]
    nn = nn[1:]
  if n == '':
    print(i)
    break
