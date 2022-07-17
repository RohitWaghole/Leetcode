class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        l = []
        for m in range(len(nums[0])):
            d=[]
            c=len(nums[0])-1-m
            for i in range(len(nums)):
                d.append([int(nums[i][c:]),i])
            
            d.sort()
            l.append(d)
        
        ans = []
        for a,b in queries:
            ans.append(l[b-1][a-1][1])
        return ans