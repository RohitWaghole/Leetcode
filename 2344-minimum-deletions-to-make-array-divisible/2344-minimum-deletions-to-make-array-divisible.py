class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        s = {}
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        t = {}
        for i in numsDivide:
            if i not in t:
                t[i]=1
        res = -1
        c=0
        m=0
        for i in sorted(s.keys()):
            f=0
            for val in t.keys():
                if val%i!=0:
                    f=1
                    m+=1
                    c+=s[i]
                    break
            
            if f==0:
                break
        return res if m==len(s.keys()) else c