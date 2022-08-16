class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        diff = float('inf')
        ans = 0
        
        for i in range(len(nums)):
            
            a = nums[i]
            start = i+1
            end = len(nums)-1
            
            while start<end:
                
                b = nums[start]
                c = nums[end]
                
                s = a+b+c
                
                if s==target:
                    return target
                
                if abs(s-target)<diff:
                    diff = abs(s-target)
                    ans = s
                    
                if s > target:
                    end -= 1
                else:
                    start += 1
                    
        return ans