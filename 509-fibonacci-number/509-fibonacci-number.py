# class Solution:
#     def fib(self, n: int) -> int:
#         a,b=0,1
#         for i in range(n):
#             c = a+b
#             a = b
#             b = c
#         return a

#####################################################################################################

# class Solution:
#     def __init__(self):
#         self.l=[]
#         a,b=0,1
#         for i in range(31):
#             self.l.append(a)
#             c = a+b
#             a = b
#             b = c
#     def fib(self, n: int) -> int:
#         return self.l[n]
    
#######################################################################################################

# class Solution:
#     def fib(self, n: int) -> int:
#         return self.getfib(n)
    
#     def getfib(self,n):
#         if n<=1:
#             return n
#         return self.getfib(n-1) + self.getfib(n-2)

#########################################################################################################

# Binet's Formula for the nth Fibonacci number

# import math
# class Solution:
#     def fib(self, n: int) -> int:
#         root5 = math.sqrt(5)
#         phi1 = (1 + root5)/2
#         phi2 = (1 - root5)/2
#         return int(round(((phi1**n)-(phi2**n))/root5))

#########################################################################################################


class Solution:
    def fib(self, n: int) -> int:
        root5 = 5**0.5
        phi = (1 + root5)/2
        return int(((phi**n) + 1)/root5)