class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        major = len(nums)//3
        res = []
        
        for i in set(nums):
            if nums.count(i)>major:
                res.append(i)
                
        return res
    
############################################################################################

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         majority = len(nums)//3
        
#         d = Counter(nums)
#         result = []
        
#         for key,val in d.items():
#             if val>majority:
#                 result.append(key)
        
#         return result