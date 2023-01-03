# 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):
    max_w, max_h = 0, 0
    
    for j in range(len(sizes)):
        # w보다 h가 크면 뒤집기
        if sizes[j][0] < sizes[j][1]:
            sizes[j][0], sizes[j][1] = sizes[j][1], sizes[j][0]
        # 가장 큰 w, h 구하기
        max_w = max(max_w, sizes[j][0])
        max_h = max(max_h, sizes[j][1])
    
    return max_w * max_h
