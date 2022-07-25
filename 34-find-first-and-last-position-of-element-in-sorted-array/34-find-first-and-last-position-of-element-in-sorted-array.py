class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target and first==-1:
                first = i
                last = i
            elif nums[i]==target:
                last = i
        return [first,last]