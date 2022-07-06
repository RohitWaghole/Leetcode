class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def valid(s):
            c = 0
            for i in s:
                if i=='(':
                    c+=1
                else:
                    c-=1
                if c<0:
                    return False
            return c==0
        
        def generate(s,n):
            if len(s)==2*n:
                if valid(s):
                    self.ans.append(''.join(s))
                return
            s.append('(')
            generate(s,n)
            s.pop()
            s.append(')')
            generate(s,n)
            s.pop()
        
        self.ans = []
        generate([],n)
        return self.ans
        
        
        
        
        
        
        
##########################################################################################################
        
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
        
    
    
    
    
    
    
##########################################################################################################
    
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
        