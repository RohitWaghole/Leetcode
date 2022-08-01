# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         def f(i,j,grid):
#             if i<0 or j<0:
#                 return 0
#             if grid[i][j]==1:
#                 return 0
#             if i==0 and j==0:
#                 return 1
            
#             up = f(i-1,j,grid)
#             left = f(i,j-1,grid)
            
#             total = up+left
#             return total
        
#         m = len(grid)
#         n = len(grid[0])
        
#         return f(m-1,n-1,grid)

#################################################################################################

# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         def f(i,j,grid,dp):
#             if i<0 or j<0:
#                 return 0
#             if grid[i][j]==1:
#                 return 0
#             if i==0 and j==0:
#                 return 1
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             up = f(i-1,j,grid,dp)
#             left = f(i,j-1,grid,dp)
            
#             dp[i][j] = up+left
#             return dp[i][j]
        
#         m = len(grid)
#         n = len(grid[0])
        
#         dp = [[-1]*n for i in range(m)]
        
#         return f(m-1,n-1,grid,dp)

# #################################################################################################

# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         def f(m,n,grid,dp):
#             if grid[0][0] == 1:
#                 return 0
            
#             for i in range(m):
#                 for j in range(n):
#                     if i==0 and j==0:
#                         dp[i][j] = 1
#                     elif grid[i][j]==1:
#                         dp[i][j] = 0
#                     else:
#                         up,left=0,0
#                         if i>0: up = dp[i-1][j]
#                         if j>0: left = dp[i][j-1]
#                         dp[i][j] = up+left
#             return dp[m-1][n-1]
            
        
#         m = len(grid)
#         n = len(grid[0])
        
#         dp = [[-1]*n for i in range(m)]
        
#         return f(m,n,grid,dp)
    

#################################################################################################

# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         def f(m,n,grid):
#             if grid[0][0] == 1:
#                 return 0
            
#             prev = [0]*n
#             for i in range(m):
#                 temp = [0]*n
#                 for j in range(n):
#                     if i==0 and j==0:
#                         temp[j] = 1
#                         continue
                    
#                     if grid[i][j]==0:
#                         up,left=0,0
#                         if i>0: up = prev[j]
#                         if j>0: left = temp[j-1]
#                         temp[j] = up+left
#                 prev = temp
#             return prev[n-1]
            
        
#         m = len(grid)
#         n = len(grid[0])
        
        
#         return f(m,n,grid)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        prev = [0]*n
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if grid[i][j]==1:
                    continue
                if i==0 and j==0:
                    curr[j] = 1
                    continue
                up,left = 0,0
                up = prev[j]
                if j>0: left = curr[j-1]
                curr[j] = up + left
            prev = curr
        return prev[n-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    