class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        l = [0,1]+[0]*(n-1)
        for i in range(1,n+1):
            if i*2+1<=n:
                l[i*2] = l[i]
                l[i*2+1] = l[i] + l[i+1]
        return max(l)