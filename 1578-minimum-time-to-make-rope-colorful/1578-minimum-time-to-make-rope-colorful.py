class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        res = 0
        
        i = 0
        while i<len(colors):
            
            mx = 0
            s = 0
            f = 0
            while i+1 < len(colors) and colors[i]==colors[i+1]:
                s += neededTime[i]
                mx = max(mx, neededTime[i])
                f = 1
                i += 1
            if f:
                mx = max(mx, neededTime[i])
                s+=neededTime[i]
                f = 0
            res += s - mx
            i += 1
        return res
            