class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        result = [None]*len(nums)
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            result[i]=s
        return result