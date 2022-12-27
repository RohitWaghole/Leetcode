class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []
        for i in range(len(capacity)):
            diff.append(capacity[i]-rocks[i])
        diff.sort()
        result = 0
        for i in diff:
            if i<=additionalRocks:
                additionalRocks -= i
                result += 1
            else:
                break
        return result