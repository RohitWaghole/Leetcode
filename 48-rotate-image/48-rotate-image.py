class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        
        temp = [[0]*n for i in range(m)]
        c = 0
        for i in matrix:
            for j in range(m):
                temp[j][n-c-1] = i[j]
            c += 1
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]