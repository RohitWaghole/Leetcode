class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         d = Counter(nums)
#         for key,val in d.items():
#             if val>(len(nums)//2):
#                 return key