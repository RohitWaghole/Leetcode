# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         d = {}
#         for i in range(len(matrix[0])):
#             d[0-i] = matrix[0][i]
#         for i in range(len(matrix)):
#             d[i] = matrix[i][0]
            
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]!=d[i-j]:
#                     return False
#         return True

####################################################################################################################

# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         d = {}
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if i-j not in d:
#                     d[i-j] = matrix[i][j]
#                 elif matrix[i][j]!=d[i-j]:
#                     return False
#         return True

####################################################################################################################

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True