class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        x = []
        for i in grid:
            x.append(i)
        
        y = []
        count = 0
        for i in range(len(grid)):
            s = []
            for j in range(len(grid)):
                s.append(grid[j][i])
            y.append(s)
        count = 0
        for i in x:
            for j in y:
                if i==j:
                    count += 1
        return count