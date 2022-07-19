class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def f(i,nums,dp):
            
            if i==0:
                return nums[i]
            if i<0:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            take = nums[i] + f(i-2,nums,dp)
            notTake = 0 + f(i-1,nums,dp)
            
            dp[i] = max(take,notTake)
            return dp[i]
        
        dp = [-1]*(len(nums)+1)
        return f(len(nums)-1,nums,dp)