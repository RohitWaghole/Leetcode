class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}
        for i in range(len(matrix[0])):
            d[0-i] = matrix[0][i]
        for i in range(len(matrix)):
            d[i] = matrix[i][0]
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]!=d[i-j]:
                    return False
        return True