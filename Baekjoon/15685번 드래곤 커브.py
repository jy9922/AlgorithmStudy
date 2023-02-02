# 드래곤 커브
# 규칙 찾기
n = int(input())

arr = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
  x, y, d, g = map(int, input().split())
  arr[x][y] = 1

  move = [d]

  # 세대만큼 반복
  for i in range(g):
    tmp = []

    # 이전 세대를 거꾸로 뒤집어서 + 1, (4일 경우 0으로)
    # 이전 세대의 인덱스를 거꾸로 접근하기
    for j in range(len(move)-1, -1, -1):
      tmp.append((move[j] + 1) % 4)
    move.extend(tmp)
    
  # move 리스트에 있는 방향대로 움직이고 방문 꼭짓점 체크
  for k in move:
    nx = x + dx[k]
    ny = y + dy[k]
    
    arr[nx][ny] = 1
    x, y = nx, ny

answer = 0
# 기준 좌표에서 아래, 오른쪽, 오른쪽 아래 좌표가 모두 1이면 answer 증가
for i in range(100):
  for j in range(100):
    if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i+1][j+1] == 1 and arr[i][j+1] == 1:
      answer += 1
print(answer)
