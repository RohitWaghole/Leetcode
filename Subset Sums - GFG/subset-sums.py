#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		self.res = []
		def f(i,s,n,arr):
		    if i>=n:
		        self.res.append(s)
		        return
            f(i+1,s+arr[i],n,arr)
            f(i+1,s,n,arr)
            
        f(0,0,N,arr)
        self.res.sort()
        return self.res
            
            
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends