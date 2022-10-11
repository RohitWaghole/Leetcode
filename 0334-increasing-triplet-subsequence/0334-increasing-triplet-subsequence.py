# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if nums[i]<nums[j]<nums[k]:
#                         return True
#         return False

##################################################################################################

# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]>=nums[j]:
#                     continue
#                 for k in range(j+1,len(nums)):
#                     if nums[j]<nums[k]:
#                         return True
#         return False

#####################################################################################################

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        nums_i = nums_j = float('inf')
        for num in nums:
            if num <= nums_i:
                nums_i = num
            elif num <= nums_j:
                nums_j = num
            else:
                return True
        return False