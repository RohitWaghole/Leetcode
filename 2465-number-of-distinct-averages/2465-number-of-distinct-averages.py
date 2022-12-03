class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        nums.sort()
        while nums!=[]:
            a = nums.pop(0)
            b = nums.pop()
            s.add((a+b)/2)
        return len(s)