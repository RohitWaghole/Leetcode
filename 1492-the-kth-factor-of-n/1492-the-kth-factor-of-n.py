# class Solution:
#     def kthFactor(self, n: int, k: int) -> int:
        
#         factors = []
#         for i in range(1,n+1):
#             if n%i == 0:
#                 factors.append(i)
#         if len(factors)<k:
#             return -1
#         return factors[k-1]

##############################################################################

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        f1, f2 = [],[]
        
        for i in range(1,int(sqrt(n))+1):
            
            if n%i==0:
                f1.append(i)
                f2.append(n//i)
        
        if f1[-1] == f2[-1]:
            f2.pop()
            
        factors = f1 + f2[::-1]
        
        return -1 if len(factors) < k else factors[k-1]