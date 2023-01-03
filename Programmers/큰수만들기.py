# 큰 수 만들기
# k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 출력

# stack을 이용한 풀이
def solution(number, k):
    answer = ''
    stack = []
    stack.append(number[0])
    
    for i in range(1, len(number)):
        # k가 0이상이고 stack의 가장 맨 위 수가 다음 숫자보다 작을 때까지 빼기
        while k > 0 and stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    
    # k가 0 이상일 때,
    while k > 0 and stack:
            stack.pop()
            k -= 1
            
    return ''.join(stack)
