class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        result = 0
        for i in nums:
            if i==0:
                c+=1
            else:
                result += (c*(c+1)//2)
                c = 0
        result += (c*(c+1)//2)
        return result