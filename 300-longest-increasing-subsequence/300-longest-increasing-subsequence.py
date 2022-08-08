# 1. RECURSION -> TIME LIMIT EXCEED

# T.C. -> O(2^N)
# S.C. -> O(N) + O(N)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         self.mx = 1
#         def f(i,ds):
            
#             if i==n:
#                 self.mx = max(self.mx, len(ds)-1)
#                 return
            
#             if nums[i]>ds[-1]:
#                 ds.append(nums[i])
#                 f(i+1,ds)
#                 ds.pop()
#             f(i+1,ds)
            
#         f(0,[-float('inf')])
#         return self.mx

############################################################################################

# TIME LIMIT EXCEED

# T.C. -> O(2^N)
# S.C. -> O(N)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
        
#         def f(i,prev):
#             if i>=n:
#                 return 0
#             res = 0 + f(i+1,prev)
            
#             if prev==-1 or nums[i]>nums[prev]:
                
#                 res = max(res, 1 + f(i+1, i))
                
#             return res
        
#         return f(0,-1)

############################################################################################

# DP WITH MEMOIZATION -> TIME LIMIT EXCEED

# T.C. -> O(N^2)
# S.C. -> O(N^2) + O(N)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [[-1]*(n+1) for i in range(n+1)]
        
#         def f(i,dp,prev):
            
#             if i>=n:
#                 return 0
#             if dp[i][prev+1]!=-1:
#                 return dp[i][prev+1]
            
#             res = 0 + f(i+1,dp,prev)
            
#             if prev == -1 or nums[i]>nums[prev]:
#                 res = max(res, 1+f(i+1,dp,i))
#             dp[i][prev+1] = res
#             return dp[i][prev+1]
        
#         return f(0,dp,-1)
        
############################################################################################

# DP WITH TABULATION -> ACCEPTED

# T.C. -> O(N^2)
# S.C. -> O(N^2)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [[0]*(n+1) for i in range(n+1)]
        
#         for i in range(n-1,-1,-1):
#             for prev in range(i-1,-2,-1):
#                 res = 0 + dp[i+1][prev+1]
#                 if prev == -1 or nums[i]>nums[prev]:
#                     res = max(res, 1+dp[i+1][i+1])
#                 dp[i][prev+1] = res
#         return dp[0][0]
        
        
############################################################################################

# T.C. -> O(N^2)
# S.C. -> O(N) + O(N)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         cur = [0]*(n+1)
#         nxt = [0]*(n+1)
        
#         for i in range(n-1,-1,-1):
#             for prev in range(i-1,-2,-1):
#                 res = 0 + nxt[prev+1]
#                 if prev==-1 or nums[i]>nums[prev]:
#                     res = max(res, 1+nxt[i+1])
#                 cur[prev+1] = res
#             nxt = cur
#         return nxt[0]
        
############################################################################################


# T.C. -> O(N^2)
# S.C. -> O(N)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n
        
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        