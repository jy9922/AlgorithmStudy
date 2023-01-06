# 조이스틱
# 알파벳 이름 완성
# 맨처음은 A
# 완성은 AAA
# 1. 위 : 다음 알파벳 
# 2. 아래 : 이전 알파벳
# 3. 왼쪽 : 커서 왼쪽 이동 (맨 앞 -> 맨 뒤)
# 4. 오른쪽 : 커서 오른쪽 이동 (맨 뒤 -> 맨 앞)
# 만들고자 하는 이름 -> 조작횟수 return

# 연속된 A의 최대 길이
# 연속된 A가 있는 곳을 갈 필요가 없음
# JAAJ인 경우 4번째 J를 처리하기 위해서 그 부분을 안가는게 효율적
# 만약 JAAJAAAJ인 경우 2,3번째 A를 건너는게 5,6,7번째 A를 건너는게 효율적

def solution(name):
    answer = 0
    
    # 기본 최소 좌우이동 횟수
    move = len(name) - 1
    
    for i, j in enumerate(name):
        # 위로 가는 것과 아래로으로 가는 것 중 작은 방향
        answer += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 왼쪽으로 가는 방식
        # 오른쪽으로 가는 방식
        print(2*i + len(name)-next)
        move = min([move, 2*i + len(name)-next, i+2*(len(name)-next)])
    answer += move
    return answer
