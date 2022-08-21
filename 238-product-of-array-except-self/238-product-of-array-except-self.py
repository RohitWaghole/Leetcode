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

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         prod = 1
#         zero = nums.count(0)
#         if zero>1: return [0]*len(nums)
        
#         for i in nums: prod *= i if i!=0 else 1
        
#         for i in range(len(nums)):
#             if zero:
#                 nums[i] = 0 if nums[i]!=0 else prod
#             else:
#                 nums[i] = prod//nums[i]
        
#         return nums

###############################################################################

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff = [], []
        s1,s2 = 1,1
        for i in range(len(nums)):
            s1 *= nums[i]
            s2 *= nums[len(nums)-i-1]
            pref.append(s1)
            suff.append(s2)
            
        suff = suff[::-1]
        n = len(nums)
        
        res = []
        for i in range(n):
            x = pref[i-1] if i else 1
            y = suff[i+1] if i+1<n else 1
            res.append(x*y)
        return res