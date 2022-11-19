# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
#         self.ans = []
#         def f(i,ds,target,candidates):
#             if target<0:
#                 return
#             if i>=len(candidates):
#                 if target==0:
#                     self.ans.append(ds[:])
#                 return
#             if candidates[i]<=target:
#                 ds.append(candidates[i])
#                 f(i,ds,target-candidates[i],candidates)
#                 ds.pop()
#             f(i+1,ds,target,candidates)
            
#         f(0,[],target,candidates)
#         return self.ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        def f(i,target,ds,candidates,res):
            if i==len(candidates):
                if target==0:
                    res.append(ds[:])
                return
            if target==0:
                res.append(ds[:])
                return
            if candidates[i]<=target:
                ds.append(candidates[i])
                f(i,target-candidates[i],ds,candidates,res)
                ds.pop()
            f(i+1,target,ds,candidates,res)
        
        res = []
        f(0,target,[],candidates,res)
        return res
        
        
        
        
        
        
        
        
        



































