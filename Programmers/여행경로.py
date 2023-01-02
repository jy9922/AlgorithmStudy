# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다.
# 항상 "ICN" 공항에서 출발합니다.

# 중요 조건
# 조건1) 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 한다.
# 조건2) 주어진 항공권은 모두 사용해야 한다.

import copy
def solution(tickets):
    answer = []
    
    # 조건 1에 맞추기 위한 정렬
    tickets.sort(key=lambda x:(x[1], x[0]))
    
    # 중복체크를 위한 리스트와 결과 리스트
    ch = [0] * (len(tickets)+1)
    res = [''] * (len(tickets) + 1)
    
    # 깊이 우선 탐색
    def DFS(L, s):
        result = []
        if L == len(tickets):
            res[L] = s[1]
            b = copy.deepcopy(res)
            answer.append(b)
            return
        else:
            for i in range(len(tickets)):
                if ch[i] == 0 and s[1] == tickets[i][0]:
                    ch[i] = 1
                    res[L] = s[1]
                    DFS(L+1, (tickets[i][0], tickets[i][1]))
                    ch[i] = 0
            
    for j in range(len(tickets)):
        # 항상 인천 공항에서 출발하고, 중복이 없는 경우 DFS 호출
        if ch[j] == 0 and tickets[j][0] == 'ICN':
            ch[j] = 1
            res[0] = tickets[j][0]
            DFS(1, (tickets[j][0], tickets[j][1]))
            ch[j] = 0
 
    return answer[0]
