class Solution:
    def countElements(self, nums: List[int]) -> int:
        l = sorted(list(set(nums)))
        d = Counter(nums)
        res = 0
        for i in range(1,len(l)-1):
            res += d[l[i]]
        return res