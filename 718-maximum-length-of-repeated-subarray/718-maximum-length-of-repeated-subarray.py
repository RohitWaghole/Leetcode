# class Solution:
#     def findLength(self, A: List[int], B: List[int]) -> int:
#         ans = 0
#         Bstarts = collections.defaultdict(list)
#         for j, y in enumerate(B):
#             Bstarts[y].append(j)

#         for i, x in enumerate(A):
#             for j in Bstarts[x]:
#                 k = 0
#                 while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
#                     k += 1
#                 ans = max(ans, k)
#         return ans
    
##########################################################################################################################################

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(length):
            seen = set(tuple(A[i:i+length]) 
                       for i in range(len(A) - length + 1))
            return any(tuple(B[j:j+length]) in seen 
                       for j in range(len(B) - length + 1))

        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1