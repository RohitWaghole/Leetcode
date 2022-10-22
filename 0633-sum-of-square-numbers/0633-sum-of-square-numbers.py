class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = {}
        for i in range(int(sqrt(c))+1):
            a = c-i**2
            d[i**2] = 1
            if a in d.keys():
                return True
        return False