class Solution:
    def isPathCrossing(self, path: str) -> bool:
        res = {'0,0':0}
        c = 1
        x,y = 0,0
        for i in path:
            if i=='N':
                y+=1
            elif i=='E':
                x+=1
            elif i=='S':
                y-=1
            else:
                x-=1
            t = str(x)+','+str(y)
            if t in res:
                return True
            res[t]=c
            c+=1
        return False