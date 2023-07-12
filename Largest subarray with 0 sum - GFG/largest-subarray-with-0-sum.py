#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        d = {}
        s = 0
        mx = 0
        k = 0
        for i in range(n):
            s += arr[i]
            if s==0:
                mx = max(mx, i+1)
            if d.get(s-k,'a')!='a':
                j = d[s-k]
                l = i-j
                mx = max(mx, l)
            
            if d.get(s,'a')=='a':
                d[s] = i
        return mx


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends