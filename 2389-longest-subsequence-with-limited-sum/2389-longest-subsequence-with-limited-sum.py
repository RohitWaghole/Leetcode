class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            c = 0
            for i in nums:
                if q>=i:
                    q -= i
                    c += 1
                else:
                    break
            ans.append(c)
        return ans