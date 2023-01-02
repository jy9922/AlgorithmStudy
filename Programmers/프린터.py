# 인쇄 요청이 들어온 순서대로 인쇄
# 중요도가 높은 문서를 먼저 인쇄하는 프린터
# 1) 인쇄 대기목록의 가장 앞에 있는 문서 꺼낸다.
# 2) 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
#    J를 대기목록의 가장 마지막에 넣는다.
# 3) 그렇지 않으면 J를 인쇄한다.
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 출력

from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    
    # 원소의 인덱스와 값 묶어서 큐에 삽입
    for idx, v in enumerate(priorities):
        q.append((idx, v))
    
    # 큐가 빌때까지 반복문
    while q:
        a = q.popleft()
        answer += 1
        
        # 큐 중에 큰 원소가 존재한다면 뒤에 추가
        for j in q:
            if a[1] < j[1]:
                q.append(a)
                answer -= 1
                break
        else:
            # 만약 찾고자하는 location이 인덱스 번호와 같다면 while문 탈출
            if a[0] == location:
                break
                
    return answer
