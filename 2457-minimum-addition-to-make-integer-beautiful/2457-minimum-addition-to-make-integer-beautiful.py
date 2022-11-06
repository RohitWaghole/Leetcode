class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        base = 0
        n0 = n
        while sum(map(int,str(n0)))>target:
            n0 = n0//10 + 1
            base += 1
            
        return n0 * (10**base) - n