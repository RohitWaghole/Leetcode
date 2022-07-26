# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
        
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return nums[i]

##############################################################################

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
        
#         d = {}
#         for i in nums:
#             d[i] = d.get(i,0)+1
#         for key,val in d.items():
#             if val>=2:
#                 return key

##############################################################################

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         for i in nums:
#             if nums[abs(i)]<0:
#                 return abs(i)
#             nums[abs(i)] *= -1

##############################################################################

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = nums[0]
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow