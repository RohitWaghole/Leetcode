# 4 solution 

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m=len(matrix)
#         n=len(matrix[0])
#         temp=[["x"]*n for i in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]==0:
#                     row=i
#                     col=j
#                     for k in range(0,n):
#                         temp[row][k]=-1
#                     for k in range(0,m):
#                         temp[k][col]=-1
                        
#         for i in range(m):
#             for j in range(n):
#                 if temp[i][j]==-1:
#                     matrix[i][j]=0
                    
        # Time= O(m*n+(m+n))
        # Space= O(m*n)
        
#####################################################################################
  
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row=i
                    col=j
                    for k in range(0,n):
                        if matrix[row][k]!=0:
                            matrix[row][k]="*"
                    for k in range(0,m):
                        if matrix[k][col]!=0:
                            matrix[k][col]="*"
                            
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="*":
                    matrix[i][j]=0
                    
                    #####################################################################################
                    
                    
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
                    
                        
                    