# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if sum(nums[i:j+1])%k==0:
#                     return True
#         return False

##########################################################################################

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:0}
        s = 0
        for i,v in enumerate(nums):
            s += v
            if s%k not in d:
                d[s%k] = i+1
            elif d[s%k]<i:
                return True
        return False