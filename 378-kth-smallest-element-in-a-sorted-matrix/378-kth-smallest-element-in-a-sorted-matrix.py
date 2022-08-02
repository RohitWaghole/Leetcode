class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l.append(matrix[i][j])
        l.sort()
        return l[k-1]

##############################################################################################

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         count = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 count+=1
#                 if count==k:
#                     return matrix[i][j]