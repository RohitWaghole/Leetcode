class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i,v in enumerate(nums):
            c = target-v
            if c in d.keys():
                return [d[c],i]
            d[v] = i    