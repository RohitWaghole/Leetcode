# T.C. -> O(N^2)
# S.C. -> O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]

#######################################################################################################################################################################

# T.C. -> O(N)
# S.C. -> O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            c = target-v
            if c in d.keys():
                return [d[c],i]
            d[v] = i    
