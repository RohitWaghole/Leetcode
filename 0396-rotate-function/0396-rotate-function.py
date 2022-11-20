# class Solution:
#     def maxRotateFunction(self, nums: List[int]) -> int:
        
#         mx = 0
#         l = len(nums)
#         for i in range(len(nums)):
#             s = 0
#             if l!=len(nums):
#                 x = nums[l:] + nums[:l]
#             else:
#                 x = nums[:l]
                
#             l-=1
            
#             for i in range(len(nums)):
#                 s += i*x[i]
                
#             mx = max(mx,s)
#         return mx

########################################################################################

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        res = -float('inf')
        s = sum(nums)
        n = len(nums)
        t = sum(i*t for i,t in enumerate(nums))
        while nums:
            t += s - nums.pop()*n
            res = max(res,t)
        return res