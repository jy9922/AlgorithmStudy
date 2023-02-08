class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        for i in stones:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        count = 0
        for j in jewels:
            if j in dic:
                count += dic[j]
            else:
                continue
        return count
 
# 두 번째 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = collections.defaultdict(int)
        count = 0
        for i in stones:
          dic[i] += 1
            
        for j in jewels:
          count += dic[j]

        return count

# 세 번째 풀이      
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = collections.Counter(stones)
        count = 0

        for j in jewels:
            count += dic[j]
    
        return count      

# 네 번째 풀이 - 리스트 컴프리헨션 이용
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
