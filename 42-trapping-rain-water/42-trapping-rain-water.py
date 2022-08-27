# class Solution:
#     def trap(self, height: List[int]) -> int:
        
#         n = len(height)
#         res = 0
#         max1, max2 = 0, 0
#         prefix = [0]*n
#         suffix = [0]*n
        
#         for i in range(n):
#             max1 = max(max1, height[i])
#             max2 = max(max2, height[n-i-1])
#             prefix[i] = max1
#             suffix[n-i-1] = max2
        
#         for i in range(n):
#             res += ( min(prefix[i], suffix[i]) - height[i] )
        
#         return res

########################################################################################################

class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax, rightMax = 0, 0
        totalWater = 0
        
        left, right = 0, len(height)-1
        
        while left<=right:
            
            if leftMax <= rightMax:
                leftMax = max(leftMax, height[left])
                totalWater += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                totalWater += rightMax - height[right]
                right -= 1
                
        return totalWater