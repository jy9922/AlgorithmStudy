class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            dic = collections.defaultdict(int)
            total = 0
            for j in range(i, len(s)):
                if dic[s[j]] == 1:
                    break
                else:
                    total += 1
                    dic[s[j]] += 1
            count = max(count, total)
        return count
      
# 슬라이딩 윈도우 문제 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 키 : 문자, 값은 : 현재 문자의 위치 (해시 테이블)
        used = {}
        max_length = start = 0
        for idx, char in enumerate(s):
            # 이미 등장했고, start가 뒤에 있다면 start 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)
            used[char] = idx
        return max_length
