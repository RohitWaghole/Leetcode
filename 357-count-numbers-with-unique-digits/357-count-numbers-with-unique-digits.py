class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        ans,curr=1,1
        choices = [9,9,8,7,6,5,4,3,2,1]
        for i in range(n):
            curr *= choices[i]
            ans += curr
        return ans