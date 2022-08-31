class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n = len(grid), len(grid[0])
        
        def dfs(i,j,grid):
            if i<0 or j<0 or i==m or j==n or grid[i][j]!='1':
                return
            grid[i][j] = '#'
            
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)
        
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j,grid)
                    result += 1
        return result