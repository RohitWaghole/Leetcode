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

class Solution:
    def fib(self, n: int) -> int:
        return self.getfib(n)
    
    def getfib(self,n):
        if n<=1:
            return n
        return self.getfib(n-1) + self.getfib(n-2)