# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
        
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return nums[i]

##############################################################################

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for key,val in d.items():
            if val>=2:
                return key