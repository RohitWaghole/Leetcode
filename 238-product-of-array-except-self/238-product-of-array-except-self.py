# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         ans = []
#         for i in range(len(nums)):
#             prod = 1
#             for j in range(len(nums)):
#                 if i!=j: prod *= nums[j]
#             ans.append(prod)
#         return ans

###############################################################################

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        zero = nums.count(0)
        if zero>1: return [0]*len(nums)
        
        for i in nums: prod *= i if i!=0 else 1
        
        for i in range(len(nums)):
            if zero:
                nums[i] = 0 if nums[i]!=0 else prod
            else:
                nums[i] = prod//nums[i]
        
        return nums