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

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def f(ind, buy):
            if ind == len(prices):
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            
            profit = 0
            if buy:
                profit = max(-prices[ind] + f(ind+1, 0), 0 + f(ind+1, 1))
            else:
                profit = max(prices[ind] + f(ind+1, 1), 0 + f(ind+1, 0))
            
            dp[ind][buy] = profit
            
            return profit
        
        
        dp = [[-1]*2 for i in range(len(prices))]
        return f(0,1)