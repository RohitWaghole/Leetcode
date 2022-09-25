# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
        
#         c = 0
#         if low>high:
#             return c
#         for i in range(low, high+1):
#             if i%2!=0:
#                 c += 1
#         return c

###########################################################################

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        return (high+1)//2 - low//2