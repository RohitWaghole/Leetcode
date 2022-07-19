# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         def f(i,nums):
            
#             if i==0:
#                 return nums[i]
#             if i<0:
#                 return 0
            
            
#             take = nums[i] + f(i-2,nums)
#             notTake = 0 + f(i-1,nums)
            
#             return max(take,notTake)
        
#         return f(len(nums)-1,nums)


##########################################################################################################


# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         def f(i,nums,dp):
            
#             if i==0:
#                 return nums[i]
#             if i<0:
#                 return 0
            
#             if dp[i]!=-1:
#                 return dp[i]
            
#             take = nums[i] + f(i-2,nums,dp)
#             notTake = 0 + f(i-1,nums,dp)
            
#             dp[i] = max(take,notTake)
#             return dp[i]
        
#         dp = [-1]*(len(nums)+1)
#         return f(len(nums)-1,nums,dp)


##########################################################################################################


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1]*(len(nums))
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            take = nums[i]
            if i>1:
                take += dp[i-2]
            notTake = 0 + dp[i-1]
            
            dp[i] = max(take,notTake)
        return dp[-1]