# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
#         def generate(ind,nums,ds,ans):
            
#             ans.append(ds[:])
            
#             for i in range(ind,len(nums)):
                
#                 if i!=ind and nums[i]==nums[i-1]:
#                     continue
#                 ds.append(nums[i])
#                 generate(i+1,nums,ds,ans)
#                 ds.pop()
            
#         nums.sort()
#         ans = []
#         generate(0,nums,[],ans)
#         return ans



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        def f(ind,nums,ds,res):
            res.append(ds[:])
            
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                f(i+1,nums,ds,res)
                ds.pop()
        res = []
        f(0,nums,[],res)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        