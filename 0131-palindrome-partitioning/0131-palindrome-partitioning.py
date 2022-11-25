class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def f(ind, s, ds, res):
            if ind == len(s):
                res.append(ds[:])
                return
            
            for i in range(ind,len(s)):
                t = s[ind:i+1]
                if t==t[::-1]:
                    ds.append(t)
                    f(i+1,s,ds,res)
                    ds.pop()
        res = []
        f(0,s,[],res)
        return res