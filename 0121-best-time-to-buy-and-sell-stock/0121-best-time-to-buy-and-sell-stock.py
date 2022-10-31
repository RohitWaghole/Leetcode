# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1,len(prices)):
#                 if prices[j]>prices[i]:
#                     profit = max(profit, prices[j]-prices[i])
#         return profit
        
###################################################################################

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         buy,sell = float('inf'),0
#         for stock in prices:
#             buy = min(buy, stock)
#             sell = max(sell, stock - buy)
#         return sell

####################################################################################

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         buy, sell = prices[0],0
#         for stock in prices:
#             if stock<buy:
#                 buy = stock
#             if stock - buy > sell:
#                 sell = stock - buy
#         return sell














class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b,s = prices[0],0
        for i in prices:
            if i<b:
                b = i
            if i-b>s:
                s = i-b
        return s


































