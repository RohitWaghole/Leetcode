class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return max([-abs(a),a] for a in nums)[1]