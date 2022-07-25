class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx, s = nums[0],0
        for i in range(len(nums)):
            s += nums[i]
            mx = max(mx,s)
            if s<0:
                s = 0
        return mx