# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
        
#         mx = -float('inf')
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     mx = max(mx,nums[i]*nums[j]*nums[k])
                     
#         return mx

#######################################################################################

class Solution:
    def maximumProduct(self, A: List[int]) -> int:
        
        A.sort()
        return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])