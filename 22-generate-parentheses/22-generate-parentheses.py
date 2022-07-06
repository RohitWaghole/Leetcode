# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
        
#         def valid(s):
#             c = 0
#             for i in s:
#                 if i=='(':
#                     c+=1
#                 else:
#                     c-=1
#                 if c<0:
#                     return False
#             return c==0
        
#         def generate(s,n):
#             if len(s)==2*n:
#                 if valid(s):
#                     self.ans.append(''.join(s))
#                 return
#             s.append('(')
#             generate(s,n)
#             s.pop()
#             s.append(')')
#             generate(s,n)
#             s.pop()
        
#         self.ans = []
#         generate([],n)
#         return self.ans
        
        
#########################################################################################################
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.ans = []
        
        def backtrack(s,l,r,n):
            if len(s)==2*n:
                self.ans.append(''.join(s))
                return
            if l<n:
                s.append('(')
                backtrack(s,l+1,r,n)
                s.pop()
            if r<l:
                s.append(')')
                backtrack(s,l,r+1,n)
                s.pop()
                
        backtrack([],0,0,n)
        return self.ans
    
    
##########################################################################################################
    
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
        