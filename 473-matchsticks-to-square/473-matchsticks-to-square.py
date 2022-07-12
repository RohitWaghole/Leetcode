# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
        
# #    USING RECURSION -> TLE    

#         s = sum(matchsticks)
#         sides = s//4
#         if sides*4!=s:
#             return False
#         sums = [0]*4
        
#         matchsticks.sort(reverse=True)
        
#         def backtrack(i):
#             if i==len(matchsticks):
#                 return sums[0]==sums[1]==sums[2]==sides
            
#             for j in range(4):
#                 if sums[j] + matchsticks[i] <= sides:
#                     sums[j] += matchsticks[i]
#                     if backtrack(i+1):
#                         return True
#                     sums[j] -= matchsticks[i]
#             return False
#         return backtrack(0)

##############################################################################################################

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        side = sum(matchsticks)//4
        if sum(matchsticks)%4!=0:
            return False
        if side != sum(matchsticks)/4:
            return False
        matchsticks.sort(reverse=True)
        def dfs(a,b,c,d,i):
            if i==len(matchsticks):
                if a==b==c==d:
                    return True
                return False
            
            if a + matchsticks[i] <= side and dfs(a+matchsticks[i],b,c,d,i+1):
                return True
            if b + matchsticks[i] <= side and dfs(a,b+matchsticks[i],c,d,i+1):
                return True
            if c + matchsticks[i] <= side and dfs(a,b,c+matchsticks[i],d,i+1):
                return True
            if d + matchsticks[i] <= side and dfs(a,b,c,d+matchsticks[i],i+1):
                return True
            return False
        return dfs(0,0,0,0,0)