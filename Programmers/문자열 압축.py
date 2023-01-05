# 문자열 압축
# 초기 문자열을 슬라이싱해서 
# 다음 문자열과 비교하면서 count 값을 증가시킨다
def solution(s):
    answer = 100000
    # s의 길이가 1인 경우를 위해 len(s)//2+2
    for i in range(1, len(s)//2+2):
        cnt = 1
        res = ''
        tmp = s[:i]
        
        # i부터 i만큼 인덱싱한 결과가 초기 인덱싱과 같은지
        for j in range(i, len(s)+i, i):
            # 같다면 cnt + 1
            if tmp == s[j:j+i]:
                cnt += 1
            # 다른 부분이 나온다면
            else:
                # cnt가 1인지, 아닌지 확인
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                # cnt 초기화 및 tmp 업데이트
                cnt = 1
                tmp = s[j:j+i]
        # 길이가 가장 작은 배열의 길이 구하기
        answer = min(answer, len(res))
    return answer
