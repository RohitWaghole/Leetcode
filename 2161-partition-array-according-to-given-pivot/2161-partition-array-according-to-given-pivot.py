class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left = []
        right = []
        
        common = []
        
        for i in nums:
            if i==pivot:
                common.append(i)
            elif i>pivot:
                right.append(i)
            else:
                left.append(i)
                
        left = left + common + right
        
        return left