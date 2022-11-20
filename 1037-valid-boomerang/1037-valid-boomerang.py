class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points.sort()
        a,b,c = points
        
        '''
        b1-a1     c1-b1
       ------- = ------- 
        b0-a0     c0-b0
        '''
        
        return ((b[1]-a[1])*(c[0]-b[0])) != ((b[0]-a[0])*(c[1]-b[1]))
    
    