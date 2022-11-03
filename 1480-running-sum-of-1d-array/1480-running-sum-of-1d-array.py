# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
        
#         result = [None]*len(nums)
#         s = 0
#         for i in range(len(nums)):
#             s+=nums[i]
#             result[i]=s
#         return result

#############################################################################################

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for i in range(1,len(nums)):
            nums[i] = nums[i]+nums[i-1]
        return nums