class Solution:
    def dayOfYear(self, date: str) -> int:
        
        year = int(date[:4])
        month = int(date[5:7])
        num = int(date[8:])
        
        l = [31,28,31,30,31,30,31,31,30,31,30,31]
        f = 0
        if year%400==0 and year%100==0:
            f = 1
        elif year%4==0 and year%100!=0:
            f = 1
            
        if f:
            l[1] += 1
            
        res = 0
        for i in range(1,month+1):
            if i==month:
                res += num
            else:
                res += l[i-1]
                
        return res
        