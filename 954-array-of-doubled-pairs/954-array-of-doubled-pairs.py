class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        d = Counter(arr)
        
        for x in sorted(arr,key = abs):
            if d[x] == 0:
                continue
            if d[2*x] == 0:
                return False
            
            d[x] -= 1
            d[2*x] -= 1
            
        return True