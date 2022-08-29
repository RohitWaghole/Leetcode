# USING MAP TO STORE THE DIAGONAL ELEMENTS
# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

#         d = defaultdict(list)
#         m,n = len(mat), len(mat[0])
#         for i in range(m):
#             for j in range(n):
#                 d[i-j].append(mat[i][j])
        
#         for key, val in d.items():
#             s = sorted(val)
#             d[key] = s
            
#         for i in range(m):
#             for j in range(n):
#                 diff = i-j
#                 mat[i][j] = d[diff].pop(0)
        
#         return mat

##################################################################################################

# DIRECTLY SORTING THE DEFAULTDICT USING SORTEDLIST
from sortedcontainers import SortedList
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        d = defaultdict(SortedList)
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                d[i-j].add(mat[i][j])
            
        for i in range(m):
            for j in range(n):
                diff = i-j
                mat[i][j] = d[diff].pop(0)
        
        return mat