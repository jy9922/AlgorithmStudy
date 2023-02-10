from collections import deque
def solution(x, y, n):
    dis = [0] * (y+1)
    q = deque()
    q.append(x)
    
    if x == y:
        return 0
    
    while q:
        x = q.popleft()
        if x == y:
            break
        for nx in (x+n, x*2, x*3):
            if 0 < nx <= y and dis[nx] == 0:
                dis[nx] = dis[x] + 1
                q.append(nx)
                
    return -1 if dis[y] == 0 else dis[y]
