class Solution:
    def trap(self, height: List[int]) -> int:
        pref, suff = [], []
        mx = 0
        for i in height:
            mx = max(mx, i)
            pref.append(mx)
        mx = 0
        for i in height[::-1]:
            mx = max(mx,i)
            suff.append(mx)
        suff = suff[::-1]
        res = 0
        for i in range(len(height)):
            res += (min(pref[i],suff[i])-height[i])
        return res