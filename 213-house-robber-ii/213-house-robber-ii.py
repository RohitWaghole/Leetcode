# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         def f(i,nums):
#             if i<0:
#                 return 0
#             if i==0:
#                 return nums[0]
#             take = nums[i] + f(i-2,nums)
#             notTake = 0 + f(i-1,nums)
#             return max(take,notTake)
        
#         if len(nums)==1:
#             return nums[0]
        
#         a1 = nums[:len(nums)-1]
#         a2 = nums[1:]
        
#         ans1 = f(len(a1)-1,a1)
#         ans2 = f(len(a2)-1,a2)
        
#         return max(ans1,ans2)

#########################################################################################################

# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         def f(i,nums,dp):
#             if i<0:
#                 return 0
#             if i==0:
#                 return nums[0]
#             if dp[i]!=-1:
#                 return dp[i]
#             take = nums[i] + f(i-2,nums,dp)
#             notTake = 0 + f(i-1,nums,dp)
#             dp[i] = max(take,notTake)
#             return dp[i]
        
#         if len(nums)==1:
#             return nums[0]
        
#         a1 = nums[:len(nums)-1]
#         a2 = nums[1:]
        
#         ans1 = f(len(a1)-1,a1,[-1]*len(a1))
#         ans2 = f(len(a2)-1,a2,[-1]*len(a2))
        
#         return max(ans1,ans2)

#########################################################################################################

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def f(i,nums,dp):
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                take = nums[i] 
                if i>1: take += dp[i-2]
                notTake = 0 + dp[i-1]
                dp[i] = max(take,notTake)
            return dp[-1]
        
        if len(nums)==1:
            return nums[0]
        
        a1 = nums[:len(nums)-1]
        a2 = nums[1:]
        
        ans1 = f(len(a1)-1,a1,[-1]*len(a1))
        ans2 = f(len(a2)-1,a2,[-1]*len(a2))
        
        return max(ans1,ans2)