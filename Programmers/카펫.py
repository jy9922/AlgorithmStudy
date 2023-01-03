# 카펫
# 카펫을 사러 갔다가 노란색 갈색 카펫의 격자의 개수는 기억했지만
# 전체 카펫 크기는 기억하지 못함

# 입력 : 갈색 격자 수, 노란색 격자 수
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 출력 (가로길이 >= 세로길이)
def solution(brown, yellow):
    w = brown + yellow
    
    for i in range(1, w+1):
        if w % i == 0:
            # 가로 길이는 몫
            a = w // i
            # 가로 길이가 세로 길이보다 큰 경우
            if a >= i:
                # 카펫의 둘레 길이 = brown에서 4를 더한 값
                if 2*a + 2*i == brown+4:
                    return [a, i]
   
