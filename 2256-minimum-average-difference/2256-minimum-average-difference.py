class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n==1:
            return 0
        
        res = 0
        
        first = nums[0]
        second = sum(nums)-nums[0]
        
        a,b = 1,len(nums)-1
        
        mn = abs((first//a)-(second//b))
        for i in range(1,n-1):
            first += nums[i]
            second -= nums[i]
            a += 1
            b -= 1
            c = abs((first//a)-(second//b))
            if c<mn:
                mn = c
                res = i
                
        t = sum(nums)//len(nums)
        if t<mn:
            res = len(nums)-1
        return res