class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mx = -1
        t = []
        for i in nums:
            t.append([sum(int(m) for m in str(i)),i])
        t.sort(reverse=True)
        # [[9, 36], [9, 18], [7, 43], [7, 7], [4, 13]]
        for i in range(len(t)-1):
            if t[i][0]==t[i+1][0]:
                mx = max(mx,t[i][1]+t[i+1][1])
        return mx