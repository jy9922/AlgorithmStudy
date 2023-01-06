# 테이블 해시 함수
# 모두 정수 타입인 컬럼(열)들로 이루어짐
# 행(튜플)
# 첫번째 컬럼 = 기본키 (중복X)
# 1. col번째 컬럼의 값을 기준으로 오름차순 정렬
# 2. 값이 동일하면 기본키를 기준으로 내림차순
# 3. i번째 행의 튜플에 대해 각 컬럼의 갓을 i로 나눈 나머지들의 합

def solution(data, col, row_begin, row_end):
    answer = 0
    # 정렬
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    # 해시 반환
    for i in range(row_begin-1, row_end):
        result = 0
        for j in range(len(data[i])):
            result += (data[i][j] % (i+1))
        answer ^= result
    return answer
