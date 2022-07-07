#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        mx = 0
        d = {}
        s=0
        for i,v in enumerate(arr):
            s+=v
            if v==0 and mx==0:
                mx = 1
            if s==0:
                mx = i+1
            if s in d:
                mx = max(mx,i-d[s])
            else:
                d[s]=i
            
        return mx
        
        
        
        
        
        #TIME LIMIT EXCEED
        # mx = 0
        # for i in range(n):
        #     s = 0
        #     for j in range(i,n):
        #         s+=arr[j]
        #         if s==0:
        #             mx = max(mx,j-i+1)
        # return mx

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends