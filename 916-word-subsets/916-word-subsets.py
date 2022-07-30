class Solution:
    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        
        def countword(word):
            l = [0]*26
            for i in word:
                l[ord(i)-ord('a')]+=1
            return l
        
        bmax = [0]*26
        for m in b:
            for i,c in enumerate(countword(m)):
                bmax[i] = max(bmax[i],c)
        ans = []
        for i in a:
            if all(x>=y for x,y in zip(countword(i),bmax)):
                ans.append(i)
        return ans