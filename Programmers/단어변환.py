# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 
# ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

# 내 풀이
# 큐에서 꺼낸 단어와 words에 단어를 비교했을 때 단어의 개수가 불일치 하는 개수가 1인 경우
# 큐에 삽입하고 중복 체크해주면서 너비 우선 탐색(BFS)를 하면서 최소 cnt 값을 찾는다.

from collections import deque
def solution(begin, target, words):
    answer = 0
    
    # 중복 체크를 위한 리스트
    v = [0] * len(words)
    q = deque()
    q.append((begin, 0))
        
    if target in words:
        while q:
            w, cnt = q.popleft()
            if w == target:
                answer = cnt
                break
            for j in range(len(words)):
                tmp = 0
                if v[j] == 0:
                    for k in range(len(w)):
                        if w[k] != words[j][k]:
                            tmp += 1
                if tmp == 1:
                    cnt += 1
                    q.append((words[j], cnt))
                    
                    # 중복 체크
                    v[j] = 1       
    else:
        answer = 0
    return answer
