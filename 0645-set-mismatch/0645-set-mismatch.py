class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dp = [0]*(len(nums)+1)
        for i in nums:
            dp[i] += 1
        rep, mis = -1,-1
        for i,v in enumerate(dp[1:]):
            if v==0:
                mis = i+1
            if v==2:
                rep = i+1
        return [rep,mis]