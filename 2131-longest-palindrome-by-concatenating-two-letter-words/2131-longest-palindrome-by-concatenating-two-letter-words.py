class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        d = Counter(words)
        res = 0
        same = 0
        odd = 0
        sim = 0
        for i in set(words):
            if i[0]==i[1]:
                if d[i]==1:
                    same = 1
                elif d[i]%2!=0:
                    odd = 1
                    sim += d[i]-1
                else:
                    sim += d[i]
            elif d.get(i[::-1],-1)!=-1:
                mn = min(d[i],d[i[::-1]])
                res += 2*mn
                d[i]-=mn
                d[i[::-1]]-=mn
        res *= 2
        res += sim*2
        if same or odd:
            res += 2
        return res