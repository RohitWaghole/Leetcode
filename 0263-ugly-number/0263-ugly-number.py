class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n<=0:
            return False
        
        def f(n,i):
            
            while n%i==0:
                n //= i
            return n
        
        for i in (2,3,5):
            n = f(n,i)
        return n==1