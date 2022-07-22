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

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def f(i,j,grid,dp):
            if i<0 or j<0:
                return 0
            if grid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            up = f(i-1,j,grid,dp)
            left = f(i,j-1,grid,dp)
            
            dp[i][j] = up+left
            return dp[i][j]
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[-1]*n for i in range(m)]
        
        return f(m-1,n-1,grid,dp)
    
    
    
    
    
    
    
    
    
    