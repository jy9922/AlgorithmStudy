# 피로도 시스템
# 최소 필요 피로도 : 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
# 소모 피로도 : 던전을 탐험한 후 소모되는 피로도
# 하루에 한 번씩 탐험할 수 있는 던전 여러개 
# 유저가 최대한 많이 탐험하려 함

# 입력 : 유저의 현재 피로도 k, 각 던전별 최소 필요 피로도, 소모 피로도
# 유저가 탐험할 수 있는 최대 던전 수 출력

# DFS를 이용한 완전 탐색
def solution(k, dungeons):
    answer = -1
    ch = [0] * len(dungeons)
    
    # 최소 필요 피로도 내림차순으로 정렬
    dungeons.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    
    def DFS(L, s):
        nonlocal answer
        if L == len(dungeons) or s < dungeons[len(dungeons)-1][0]:
            if answer < L:
                answer = L
            return
        else:
            for i in range(len(dungeons)):
                if ch[i] == 0 and dungeons[i][0] <= s:
                    ch[i] = 1
                    re = s - dungeons[i][1]
                    DFS(L+1, re)
                    ch[i] = 0
    DFS(0, k)
                
    return answer
