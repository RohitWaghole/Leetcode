class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.ans = []
        def f(i,ds,target,candidates):
            if target<0:
                return
            if i>=len(candidates):
                if target==0:
                    self.ans.append(ds[:])
                return
            if candidates[i]<=target:
                ds.append(candidates[i])
                f(i,ds,target-candidates[i],candidates)
                ds.pop()
            f(i+1,ds,target,candidates)
            
        f(0,[],target,candidates)
        return self.ans