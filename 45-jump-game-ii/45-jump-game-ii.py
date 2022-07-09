# #TLE
# class Solution:
#     def jump(self, nums: List[int]) -> int:
        
#         jumps = [float('inf')]*len(nums)
#         jumps[0] = 0
#         for i in range(len(nums)):
#             for j in range(i):
#                 if i<=j+nums[j]:
#                     jumps[i] = min(jumps[i],jumps[j]+1)
#         return jumps[-1]

##############################################################################################################

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        left = right = 0
        while right<len(nums)-1:
            
            maxRange = 0
            for i in range(left,right+1):
                maxRange = max(maxRange, i+nums[i])
            left = right+1
            right = maxRange
            jumps += 1
        return jumps