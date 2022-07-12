# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
        
#         s = 0
#         for i in range(1,num):
#             if num%i==0:
#                 s+=i
#         return s==num
    
#####################################################################################################################

# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         s = 0
#         for i in range(1,num):
#             if num%i==0:
#                 s+=i
#             if s>num:
#                 return False
#         return s==num

#####################################################################################################################

# class Solution:
#     def checkPerfectNumber(self, n: int) -> bool:
        
#         s = 0
#         for i in range(1,n//2+1):
#             if n%i==0:
#                 s+=i
#             if s>n:
#                 return False
#         return s==n

####################################################################################################################

# class Solution:
#     def checkPerfectNumber(self, n: int) -> bool:
        
#         s = 0
#         for i in range(1,n):
#             if i*i>n:
#                 break
#             if n%i==0:
#                 s+=i
#                 if i*i != n:
#                     s += n//i
#         return s-n==n
        
####################################################################################################################

class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        return n in (6,28,496,8128,33550336)
        
        
        
        