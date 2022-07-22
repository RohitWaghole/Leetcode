# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         def f(i,j):
#             if i<0 or j<0:
#                 return 0
#             if i==0 and j==0:
#                 return 1
            
#             up = f(i-1,j)
#             left = f(i,j-1)
            
#             total = up + left
#             return total
        
#         return f(m-1,n-1)

#####################################################################################################

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         def f(i,j,dp):
#             if i<0 or j<0:
#                 return 0
#             if i==0 and j==0:
#                 return 1
#             if dp[i][j]!=-1:
#                 return dp[i][j]
            
#             up = f(i-1,j,dp)
#             left = f(i,j-1,dp)
            
#             dp[i][j] = up + left
#             return dp[i][j]
        
#         dp = [[-1]*n for i in range(m)]
#         return f(m-1,n-1,dp)


#####################################################################################################

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*n for i in range(m)]
        
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = 1
                    continue
                down,right = 0,0
                if i>0: down = dp[i-1][j]
                if j>0: right = dp[i][j-1]
                
                dp[i][j] = down + right
        return dp[m-1][n-1]
        
        
        
        
        
        
        
        
        
        
        
        