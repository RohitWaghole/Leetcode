# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return list(itertools.permutations(nums))
    
####################################################################################################################

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
        
#         def generate(ds,nums,freq,ans):
#             if len(ds)==len(nums):
#                 ans.append(ds[:])
#                 return
#             for i in range(len(nums)):
#                 if freq[i]!=1:
#                     ds.append(nums[i])
#                     freq[i]=1
#                     generate(ds,nums,freq,ans)
#                     ds.pop()
#                     freq[i]=0
#         freq = [0]*len(nums)
#         ans = []
#         generate([],nums,freq,ans)
#         return ans

#####################################################################################################################

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def generate(curr,nums,ans):
            
            if curr==len(nums): ans.append(nums[:]); return
            
            for i in range(curr,len(nums)):
                nums[curr],nums[i] = nums[i],nums[curr]
                generate(curr+1,nums,ans)
                nums[curr],nums[i] = nums[i],nums[curr]
                
        ans = []
        generate(0,nums,ans)
        return ans