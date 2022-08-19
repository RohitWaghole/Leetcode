class Solution:
    def reformat(self, s: str) -> str:
        
        n, c = '', ''
        
        for i in s:
            if i.isdigit():
                n+=i
            else:
                c+=i
                
        if abs(len(n)-len(c))>1:
            return ''
        
        res = ''
        a,b = len(n),len(c)
        
        if a>b:
            n,c = c,n
            a,b = b,a
            
        for i in range(a):
            res+=c[i]+n[i]
        
        if a!=b:
            res+=c[-1]
        return res