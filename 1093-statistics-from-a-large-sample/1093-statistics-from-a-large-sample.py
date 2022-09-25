class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
        mx = -1
        mn = -1
        
        mxf = 0
        sm = 0
        mxe = 0
        n = 0
        for i,v in enumerate(count):
            if v!=0:
                n += v
                
                if mn == -1:
                    mn = i
                
                mx = i
                
                if v>mxf:
                    mxe = i
                    mxf = v
                    
                sm += i*v
            
        mn = float(mn)
        mx = float(mx)
        mxe = float(mxe)
        avg = sm/n
        n = sum(count)
        for i in range(255):
            count[i + 1] += count[i]
        median1 = bisect.bisect(count, (n - 1) / 2)
        median2 = bisect.bisect(count, n / 2)
        med = (median1 + median2) / 2.0
            
        return [mn, mx, avg, med, mxe]