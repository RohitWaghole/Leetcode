class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l = [[-1]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:

                    row = i
                    col = j
                    for m in range(len(matrix[0])):
                        l[row][m] = 0
                    for m in range(len(matrix)):
                        l[m][col] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if l[i][j]==0:
                    matrix[i][j] = 0
