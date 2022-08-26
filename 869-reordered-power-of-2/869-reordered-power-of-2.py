# class Solution:
#     def reorderedPowerOf2(self, n: int) -> bool:
        
#         for perm in itertools.permutations(str(n)):
#             if perm[0] != '0' and bin(int(''.join(perm))).count('1')==1:
#                 return True
#         return False

##################################################################################################

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        d = collections.Counter(str(n))
        for i in range(31):
            s = collections.Counter(str(2**i))
            if s==d:
                return True
        return False