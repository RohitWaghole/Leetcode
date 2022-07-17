class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        
        return [sum(val//2 for val in d.values()),sum(val%2 for val in d.values())]