class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        c = 0
        if s%3!=0:
            return False
        target = s//3
        d = 0
        for i in arr:
            d+=i
            if d==target:
                c+=1
                d=0
        return c>=3
    
    