class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = 0
        mx = max(nums)
        mn = min(nums)
        for i in nums:
            if mn<i<mx:
                res += 1
        return res