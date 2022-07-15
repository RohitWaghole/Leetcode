# class Solution:
#     def climbStairs(self, n: int) -> int:
##      TLE
#         def f(n):
            
#             if n<0:
#                 return 0
#             if n<=1:
#                 return 1
#             return f(n-1)+f(n-2)
#         return f(n)

##################################################################################################################

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n<=2:
#             return n
#         dp = [0]*(n)
#         dp[0]=1
#         dp[1]=2
#         for i in range(2,n):
#             dp[i]=dp[i-1]+dp[i-2]
#         return dp[n-1]

####################################################################################################################

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n<=2:
#             return n
#         prev,prev2=1,2
#         for i in range(3,n+1):
#             nxt = prev+prev2
#             prev=prev2
#             prev2 = nxt
#         return nxt

####################################################################################################################

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        root5 = 5**0.5
        phi = (1+root5)/2
        fib = int((1+phi**(n+1))/root5)
        return fib