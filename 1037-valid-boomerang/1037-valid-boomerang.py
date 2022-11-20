class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points.sort()
        a,b,c = points
        
        '''
        y2b1-y1a1     y3c1-y2b1
       ------- = ------- 
        x2b0-x1a0     x3c0-x2b0
        '''
        
        return ((b[1]-a[1])*(c[0]-b[0])) != ((b[0]-a[0])*(c[1]-b[1]))