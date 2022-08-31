class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        m,n = len(land),len(land[0])
        
        def dfs(i,j):
            if i<0 or j<0 or i==m or j==n or land[i][j]!=1:
                return (0,0)
            
            land[i][j] = '#'
            
            x1, y1 = dfs(i+1, j)
            x2, y2 = dfs(i, j+1)
            
            x = max(x1, x2, i)
            y = max(y1, y2, j)
            
            return (x,y)
            
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x,y = dfs(i,j)
                    res.append([i,j,x,y])
        return res