class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        res = sSum = 0
        for e,s in sorted(zip(efficiency, speed), reverse=1):
            bisect.insort(h, -s)
            sSum += s
            if len(h) > k:
                sSum += h.pop()
            res = max(res, sSum * e)
        return res % (10**9+7)