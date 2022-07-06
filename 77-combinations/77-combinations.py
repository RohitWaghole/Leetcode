# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
        
#         l = [i for i in range(1,n+1)]
#         def f(i,k,l,ans,ds):
            
#             if i>=len(l):
#                 if len(ds)==k:
#                     ans.append(ds[:])
#                 return
#             ds.append(l[i])
#             f(i+1,k,l,ans,ds)
#             ds.pop()
#             f(i+1,k,l,ans,ds)
        
#         ans = []
#         f(0,k,l,ans,[])
#         return ans

###################################################################################################

from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations([i for i in range(1,n+1)],k)