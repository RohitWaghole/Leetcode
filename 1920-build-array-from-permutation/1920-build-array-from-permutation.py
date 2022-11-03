# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         res = [0]*len(nums)
#         for i in range(len(nums)):
#             res[i] = nums[nums[i]]
#         return res
    
##################################################################

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         res = []
#         for i in nums:
#             res.append(nums[i])
#         return res
    
#######################################################################

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]