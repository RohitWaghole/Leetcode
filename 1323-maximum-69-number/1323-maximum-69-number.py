class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ''
        f = 1
        for i in str(num):
            if int(i)==6 and f:
                res += '9'
                f = 0
            else:
                res += i
        return int(res)