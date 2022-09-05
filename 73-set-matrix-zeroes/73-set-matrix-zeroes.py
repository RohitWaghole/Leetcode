class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        temp=[["x"]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row=i
                    col=j
                    for k in range(0,n):
                        temp[row][k]=-1
                    for k in range(0,m):
                        temp[k][col]=-1
                        
        for i in range(m):
            for j in range(n):
                if temp[i][j]==-1:
                    matrix[i][j]=0
        
#####################################################################################
                    
                    
                        
                    