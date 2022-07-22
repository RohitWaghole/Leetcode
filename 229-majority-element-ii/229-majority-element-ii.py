class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums)//3
        
        d = Counter(nums)
        result = []
        
        for key,val in d.items():
            if val>majority:
                result.append(key)
        
        return result