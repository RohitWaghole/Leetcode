# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         def f(ind, buy):
#             if ind == len(prices):
#                 return 0
            
#             profit = 0
#             if buy:
#                 profit = max(-prices[ind] + f(ind+1, 0), 0 + f(ind+1,1))
#             else:
#                 profit = max(prices[ind] + f(ind+1, 1), 0 + f(ind+1, 0))
#             return profit
#         return f(0,1)

######################################################################################

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         def f(ind, buy):
#             if ind == len(prices):
#                 return 0
#             if dp[ind][buy] != -1:
#                 return dp[ind][buy]
            
#             profit = 0
#             if buy:
#                 profit = max(-prices[ind] + f(ind+1, 0), 0 + f(ind+1, 1))
#             else:
#                 profit = max(prices[ind] + f(ind+1, 1), 0 + f(ind+1, 0))
            
#             dp[ind][buy] = profit
            
#             return profit
        
        
#         dp = [[-1]*2 for i in range(len(prices))]
#         return f(0,1)


######################################################################################

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         n = len(prices)
#         dp = [[0]*2 for _ in range(n+1)]
        
#         dp[n][0] = dp[n][1] = 0
        
#         for ind in range(n-1,-1,-1):
#             for buy in range(2):
#                 profit = 0
#                 if buy:
#                     profit = max(-prices[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
#                 else:
#                     profit = max( prices[ind] + dp[ind+1][1], 0 + dp[ind+1][0])
#                 dp[ind][buy] = profit
#         return dp[0][1]
        

######################################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curr = [0,0]
        ahead = [0,0]
        n = len(prices)
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[ind] + ahead[0], 0 + ahead[1])
                else:
                    profit = max( prices[ind] + ahead[1], 0 + ahead[0])
                curr[buy] = profit
            ahead = curr
        return ahead[1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        