# 과학자의 생산성과 영향력을 나타내는 지표
# 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문인 h번 이하 인용되었다면 h의 최댓값이 과학자의 H-Index임

def solution(citations):
    citations.sort(reverse=True)
    for idx, i in enumerate(citations):
        if idx >= i:
            return idx
    return len(citations)
