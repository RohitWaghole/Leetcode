class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        res = []
        a = intervals[0]
        for i in range(1,len(intervals)):
            
            b = intervals[i]
            
            if b[0]<=a[1]:
                a[1] = max(a[1],b[1])
            else:
                res.append(a)
                a = intervals[i]
        res.append(a)
        return res
        