class Solution:
    def countExcellentPairs(self, A: List[int], k: int) -> int:
        
        cnt = {}
        res = 0
        s = set()
        
        for i in A:
            s.add(i)
        for i in s:
            x = bin(i).count('1')
            if x in cnt:
                cnt[x]+=1
            else:
                cnt[x] = 1
                
        for i in range(1,30):
            for j in range(1,30):
                if i+j >= k:
                    res += cnt.get(i,0) * cnt.get(j,0)
        return res