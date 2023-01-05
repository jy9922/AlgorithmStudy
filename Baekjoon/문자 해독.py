# 마야 문자는 단어 기록할 때 글자를 아무렇게 배열함
# 고고학자는 W라는 특저 단어를 발굴 기록으로부터 찾고있음
# 문자열 S 안에서 문자열 W의 순열 중 하나가 부분 문자열로 들어있는 경우의 수

g, l = map(int, input().split())
w = input()
s = input()

# 단어와 문자열 배열 형식으로 초기화
w1 = [0] * 52
s1 = [0] * 52

# 배열의 인덱스 : 각 문자의 번호
# w에 문자가 있다면 해당 인덱스에 +1
for i in range(g):
  if 'a' <= w[i] <= 'z':
    w1[ord(w[i]) - ord('a')] += 1
  else:
    w1[ord(w[i]) - ord('A') + 26] += 1

length, start, cnt = 0,0,0

# 윈도우 슬라이싱으로 특정 범위를 한칸씩 옮겨가며 비교
for j in range(l):
  # 문자열이 소문자 사이라면 
  if 'a' <= s[j] <= 'z':
    s1[ord(s[j]) - ord('a')] += 1
  else:
    s1[ord(s[j]) - ord('A') + 26] += 1
  length += 1
  
  # 만약 범위가 같다면
  if length == g:
    # 배열이 같은지 확인
    if w1 == s1:
      cnt += 1
    # start 값에 해당되는 값 해제
    if 'a' <= s[start] <= 'z':
      s1[ord(s[start]) - ord('a')] -= 1
    else:
      s1[ord(s[start]) -  ord('A') + 26] -= 1
    # start 한칸 옮기기
    start += 1
    # 길이 줄이기
    length -= 1
print(cnt)
