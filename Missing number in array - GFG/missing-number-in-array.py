#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        x = 0
        for i in array:
            x^=i
        for i in range(1,n+1):
            x^=i
        return x
        

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