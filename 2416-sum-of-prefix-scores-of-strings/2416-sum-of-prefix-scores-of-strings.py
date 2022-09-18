class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        lst = []
        for i in words:
            r = ''
            for w in i:
                r += w
                lst.append(r)
            lst.append(0)
        d = Counter(lst)
        res = []
        c = 0
        for i in lst:
            if i!=0:
                c += d[i]
            else:
                res.append(c)
                c = 0
        return res