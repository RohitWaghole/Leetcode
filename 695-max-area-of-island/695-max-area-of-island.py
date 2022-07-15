# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
#         seen = set()
        
#         def maxArea(r,c):
            
#             if not (0<=r<len(grid) and 0<=c<len(grid[0]) and (r,c) not in seen and grid[r][c]):
#                 return 0
            
#             seen.add((r,c))
            
#             left = maxArea(r,c-1)
#             right = maxArea(r,c+1)
#             up = maxArea(r-1,c)
#             down = maxArea(r+1,c)
            
#             return (1+left+right+up+down)
        
#         return max(maxArea(r,c)
#                    for r in range(len(grid))
#                    for c in range(len(grid[0])))

##################################################################################################################

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def maxArea(r,c):
            
            count = 0
            if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]) and grid[r][c]==1:
                grid[r][c]=0
                count += 1
                count += maxArea(r+1,c)
                count += maxArea(r-1,c)
                count += maxArea(r,c+1)
                count += maxArea(r,c-1)
                
            return count
        
        MaxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                MaxArea = max(MaxArea, maxArea(r,c))
        return MaxArea