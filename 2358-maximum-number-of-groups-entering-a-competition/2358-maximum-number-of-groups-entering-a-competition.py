class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        grades.sort()
        res = 0
        count,prevc = 0,0
        sum, prevs = 0,0
        
        for i in grades:
            sum += i
            count += 1
            if sum>prevs and count>prevc:
                res+=1
                prevs = sum
                prevc = count
                sum = 0
                count = 0
        return res