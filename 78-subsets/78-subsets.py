# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
        
# #         1. Using Recursion
# #         def sub(index,nums,ds,ans):
# #             if index >= len(nums):
# #                 ans.append(ds[:])
# #                 return
            
# #             ds.append(nums[index])
# #             sub(index+1,nums,ds,ans)
# #             ds.pop()
# #             sub(index+1,nums,ds,ans)
        
# #         ans=[]
# #         sub(0,nums,[],ans)
# #         return ans

#         # 2. simple Method
    
#         ans = [[]]
        
#         for i in nums:
#             ans += [j + [i] for j in ans]
            
#         return ans



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
#         1. Using Recursion

        def generate(i,ds,nums,ans):
            
            if i>=len(nums):
                ans.append(ds[:])
                return
            ds.append(nums[i])
            generate(i+1,ds,nums,ans)
            ds.pop()
            generate(i+1,ds,nums,ans)
            
        ans = []
        generate(0,[],nums,ans)
        return ans






























