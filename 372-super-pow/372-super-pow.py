# class Solution:
#     def superPow(self, a: int, b: List[int]) -> int:
#         b = int(''.join(str(i) for i in b))
#         return pow(a,b)%1337

#################################################################

# class Solution:
#     def superPow(self, a: int, b: List[int]) -> int:
        
#         b = int(''.join(str(i) for i in b))
        
#         ans = 1
#         while b>0:
#             if b%2==1:
#                 ans *= a
#                 b -= 1
#             else:
#                 a *= a
#                 b //= 2
#         return ans%1337


#################################################################

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(''.join(map(str, b))), 1337)

