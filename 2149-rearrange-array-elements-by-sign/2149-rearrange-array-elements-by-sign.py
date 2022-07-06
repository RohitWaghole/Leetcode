class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos,neg = [],[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
                
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result