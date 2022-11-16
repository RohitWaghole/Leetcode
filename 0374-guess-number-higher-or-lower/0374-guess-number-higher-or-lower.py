# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        start = 1
        end = n
        while 1:
            
            mid = start + (end - start)//2
            
            t = guess(mid)
            if t==0:
                return mid
            
            if t==-1:
                end = mid - 1
            else:
                start = mid + 1