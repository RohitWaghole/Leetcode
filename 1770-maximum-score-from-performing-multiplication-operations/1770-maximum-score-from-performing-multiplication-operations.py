# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
#         def f(i):
            
#             if i==len(multipliers):
#                 return 0
            
#             a = nums.pop(0)
#             start = a*multipliers[i] + f(i+1)
#             nums.insert(0,a)
#             b = nums.pop()
#             end = b*multipliers[i] + f(i+1)
#             nums.append(b)
            
#             return max(start, end)
        
#         return f(0)

###########################################################################################################

# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
#         dp = [[-1]*len(multipliers) for i in range(len(multipliers))]
        
#         def f(i,j):
#             if i==len(multipliers):
#                 return 0
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             a = nums.pop(0)
#             start = a*multipliers[i] + f(i+1,j+1)
#             nums.insert(0,a)
#             b = nums.pop()
#             end = b*multipliers[i] + f(i+1,j)
#             nums.append(b)
            
#             dp[i][j] = max(start, end)
            
#             return dp[i][j]
        
#         return f(0,0)

###########################################################################################################

# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
#         dp = {}
        
#         def f(i,j):
#             if i==len(multipliers):
#                 return 0
            
#             if (i,j) in dp:
#                 return dp[(i,j)]
            
#             a = nums.pop(0)
#             start = a*multipliers[i] + f(i+1,j+1)
#             nums.insert(0,a)
#             b = nums.pop()
#             end = b*multipliers[i] + f(i+1,j)
#             nums.append(b)
            
#             dp[(i,j)] = max(start, end)
            
#             return dp[(i,j)]
        
#         return f(0,0)
            

###########################################################################################################

# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
#         n = len(nums)
#         m = len(multipliers)
        
#         dp = [[0]*(m+1) for i in range(m+1)]
        
#         for i in range(m-1,-1,-1):
#             for j in range(i,-1,-1):
            
#                 start = nums[j] * multipliers[i] + dp[i+1][j+1]
#                 end = nums[(n-1)-(i-j)] * multipliers[i] + dp[i+1][j]

#                 dp[i][j] = max(start, end)
#         return dp[0][0]


###########################################################################################################

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        n = len(nums)
        m = len(multipliers)
        
        dp = [0]*(m+1)
        
        for i in range(m-1,-1,-1):
            next_row = dp.copy()
            for j in range(i,-1,-1):
            
                start = nums[j] * multipliers[i] + next_row[j+1]
                end = nums[(n-1)-(i-j)] * multipliers[i] + next_row[j]

                dp[j] = max(start, end)
        return dp[0]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        