# # class Solution:
# #     def canJump(self, nums: List[int]) -> bool:
        
# #         # TRAVERSE FROM BACKWARDS UNTIL GOAL BECOMES FIRST INDEX
# #         goal = len(nums)-1
        
# #         for i in range(len(nums)-1,-1,-1):
# #             if i+nums[i]>=goal:
# #                 goal = i
# #         return goal==0

# #############################################################################################################

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         reachable = 0
#         for i in range(len(nums)):
#             if i>reachable:
#                 return False
#             reachable = max(reachable,i+nums[i])
            
#         return True












class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i>reachable:
                return False
            reachable = max(reachable,i+nums[i])
        return True