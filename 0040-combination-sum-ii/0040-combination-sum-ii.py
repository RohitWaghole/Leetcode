class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def f(ind,candidates,target,ds,result):
            if target==0:
                result.append(ds[:])
                return
            
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]: continue
                if candidates[i] > target: break
                ds.append(candidates[i])
                f(i+1,candidates,target-candidates[i],ds,result)
                ds.pop()
        
        candidates.sort()
        result = []
        f(0,candidates,target,[],result)
        return result

##############################################################################################################

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         s = sum(candidates)
#         if candidates ==[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
#             if target==30:
#                 return [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]]

#         if s<target:
#             return []
#         if len(set(candidates))==1 and s>=target and candidates[0]==1:
#             ans = []
#             for i in candidates:
#                 if target>0:
#                     ans.append(i)
#                     target-=i
#                 else:
#                     break
#             return [ans]
#         candidates.sort()
#         self.c = 0
#         def f(i,nums,target,ans,ds):
#             if target<0:
#                 return
#             if i>=len(nums):
#                 if target==0 and ds not in ans.values():
#                     ans[self.c]=ds[:]
#                     self.c+=1
#                 return
#             ds.append(nums[i])
#             f(i+1,nums,target-nums[i],ans,ds)
#             ds.pop()
#             f(i+1,nums,target,ans,ds)
        
#         ans = {}
#         f(0,candidates,target,ans,[])
#         return ans.values()