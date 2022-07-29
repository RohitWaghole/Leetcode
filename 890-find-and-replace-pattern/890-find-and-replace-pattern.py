class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for i in words:
            f=1
            m1, m2 = {}, {}
            for w, p in zip(i, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    f=0
                    break
            if f:
                ans.append(i)
        return ans