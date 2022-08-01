# 1. Using Recursion

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         mn = float('inf')
#         def f(m,n,grid):
#             if m==0 and n==0:
#                 return grid[m][n]
#             if m<0 or n<0:
#                 return 2000000000
#             up = grid[m][n] + f(m-1,n,grid)
#             left = grid[m][n] + f(m,n-1,grid)
#             return min(up,left)
#         ans = f(m-1,n-1,grid)
#         return ans
    
##########################################################################################################

# Using Dynamic Programming - Memoization

# class Solution:
#     def helper(self, x, y, grid, cost):
#         M, N = len(grid), len(grid[0])
#         if x == M or y == N:
#             return float('inf')
#         elif cost[x][y] != -1:
#             return cost[x][y]
#         else:
#             right, down = self.helper(x,y+1,grid,cost), self.helper(x+1,y,grid,cost)
#             cost[x][y] = min(right, down) + grid[x][y]
#         return cost[x][y]
    
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         M, N = len(grid), len(grid[0])
#         cost = [[-1]*N for _ in range(M)]
#         cost[M-1][N-1] = grid[M-1][N-1]
#         return self.helper(0, 0, grid, cost)

############################################################################################################

# Using DP - Tabulation -> O(MN) space complexity


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m,n = len(grid), len(grid[0])
#         dp = [[0]*n for i in range(m)]
#         dp[0][0] = grid[0][0]
#         for i in range(1,m):
#             dp[i][0] = grid[i][0] + dp[i-1][0]
#         for j in range(1,n):
#             dp[0][j] = grid[0][j] + dp[0][j-1]
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
#         return dp[m-1][n-1]
        
##############################################################################################################

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
        
#         m,n = len(grid), len(grid[0])
#         dp = [[0]*n for _ in range(m)]
        
#         for i in range(m):
#             for j in range(n):
#                 if i==0 and j==0:
#                     dp[i][j] = grid[0][0]
#                 else:
#                     up,left = 0,0
#                     if i>0: 
#                         up = grid[i][j] + dp[i-1][j]
#                     else:
#                         up = float('inf')
#                     if j>0: 
#                         left = grid[i][j] + dp[i][j-1]
#                     else:
#                         left = float('inf')
#                     dp[i][j] = min(up,left)
#         return dp[m-1][n-1]


##########################################################################################################


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        
        prev = [0]*m
        
        for i in range(m):
            cur = [0]*n
            for j in range(n):
                if i==0 and j==0:
                    cur[j] = grid[0][0]
                else:
                    up,left = 0,0
                    # previous things
                    if i>0: 
                        up = grid[i][j] + prev[j]
                    else:
                        up = float('inf')
                    # current things
                    if j>0: 
                        left = grid[i][j] + cur[j-1]
                    else:
                        left = float('inf')
                    cur[j] = min(up,left)
            prev = cur
        return prev[n-1]
        