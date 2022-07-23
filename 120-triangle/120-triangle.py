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

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def f(i,j,triangle,n,dp):
            
            if i==n-1:
                return triangle[n-1][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down = f(i+1,j,triangle,n,dp)
            diagonal = f(i+1,j+1,triangle,n,dp)
            dp[i][j] = min(down,diagonal) + triangle[i][j]
            return dp[i][j]
        
        n = len(triangle[-1])
        dp = [[-1]*n for i in range(n)]
        return f(0,0,triangle,n,dp)