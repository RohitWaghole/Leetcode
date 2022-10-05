'''
Recursion -> TLE
T.C. => O(N)
S.C. => O(N)(RECURSION STACK SPACE)
'''

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

'''
RECURSION + DP : MEMOIZATION -> ACCEPTED
T.C. -> O(N)
S.C. -> O(N)(ARRAY) + O(N)(RECURSION STACK SPACE)
'''

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

'''
DP + TABULATION -> ACCEPTED
T.C. -> O(N)
S.C. -> O(N)(ARRAY)
'''

# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         dp = [-1]*(len(nums))
#         dp[0] = nums[0]
#         for i in range(1,len(nums)):
#             take = nums[i]
#             if i>1:
#                 take += dp[i-2]
#             notTake = 0 + dp[i-1]
#             dp[i] = max(take,notTake)
#         return dp[-1]


##########################################################################################################

'''
TABULATION WITH SPACE OPTIMIZED -> ACCEPTED
T.C. -> O(N)
S.C. -> O(1)
'''

# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         prev2 = 0
#         prev = nums[0]
#         for i in range(1,len(nums)):
#             take = nums[i]
#             if i>1:
#                 take += prev2
#             notTake = prev
#             curi = max(take,notTake)
#             prev2 = prev
#             prev = curi
#         return prev
























class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            
            pick = nums[i]
            if i>1:
                pick += dp[i-2]
            notPick = dp[i-1]
            
            dp[i] = max(pick,notPick)
            
        return dp[-1]
        
        

































