# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         def f(i,j,triangle,n):
            
#             if i==n-1:
#                 return triangle[n-1][j]
#             down = f(i+1,j,triangle,n)
#             diagonal = f(i+1,j+1,triangle,n)
#             total = min(down,diagonal) + triangle[i][j]
#             return total
        
#         n = len(triangle[-1])
#         return f(0,0,triangle,n)

###########################################################################################

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         def f(i,j,triangle,n,dp):
            
#             if i==n-1:
#                 return triangle[n-1][j]
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             down = f(i+1,j,triangle,n,dp)
#             diagonal = f(i+1,j+1,triangle,n,dp)
#             dp[i][j] = min(down,diagonal) + triangle[i][j]
#             return dp[i][j]
        
#         n = len(triangle[-1])
#         dp = [[-1]*n for i in range(n)]
#         return f(0,0,triangle,n,dp)

# ###########################################################################################

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         def f(triangle,n,dp):
            
#             for j in range(n):
#                 dp[n-1][j] = triangle[n-1][j]
                
#             for i in range(n-2,-1,-1):
#                 for j in range(i,-1,-1):
#                     down = dp[i+1][j]
#                     diagonal = dp[i+1][j+1]
#                     dp[i][j] = min(down,diagonal) + triangle[i][j]
#             return dp[0][0]
        
#         n = len(triangle[-1])
#         dp = [[-1]*n for i in range(n)]
#         return f(triangle,n,dp)
    
###########################################################################################

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def f(triangle,n):
            
            prev = [0]*n
            for j in range(n):
                prev[j] = triangle[n-1][j]
                
            for i in range(n-2,-1,-1):
                curr = [0]*n
                for j in range(i,-1,-1):
                    down = prev[j]
                    diagonal = prev[j+1]
                    curr[j] = min(down,diagonal) + triangle[i][j]
                prev = curr
            return prev[0]
        
        n = len(triangle[-1])
        return f(triangle,n)
        