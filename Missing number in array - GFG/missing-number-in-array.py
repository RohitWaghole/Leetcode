#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        l=[0]*n
        for i in array:
            l[i-1]+=1
        for i,v in enumerate(l):
            if v==0:
                return i+1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends