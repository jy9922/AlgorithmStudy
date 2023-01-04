# 소수 찾기
# 한자리 숫자가 적힌 종이 조각들이 흩어져있다.
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아보자.

def solution(numbers):
    answer = []
    res = [0] * len(numbers)
    ch = [0] * len(numbers)
    
    # 중복 순열을 이용해서 만들 수 있는 숫자 찾기
    def DFS(L):
        if L == len(numbers):
            a = ''.join(res)
            answer.append(a)
            return
        else:
            for i in range(len(numbers)):
                if ch[i] == 0:
                    ch[i] = 1
                    res[L] = numbers[i]
                    DFS(L+1)
                    ch[i] = 0
                else:
                    res[L] = ''
                    DFS(L+1)
                
    DFS(0)  
    
    # 문자열 원소 숫자로 변환 후 중복 제거
    answer = list(map(int, answer))
    answer2 = set(answer)
    cnt = 0
    
    # 소수 검열
    for i in answer2:
        # 소수 체크 변수
        tmp = 0
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                tmp = 1
                break
        if tmp == 0:
            print(i)
            cnt += 1
    return cnt
