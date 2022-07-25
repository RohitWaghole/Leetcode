class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:

                    row = i
                    col = j
                    for m in range(len(matrix[0])):
                        if matrix[row][m]!=0: matrix[row][m] = 'a'
                    for m in range(len(matrix)):
                        if matrix[m][col]!=0: matrix[m][col] = 'a'
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='a':
                    matrix[i][j] = 0
