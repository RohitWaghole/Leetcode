#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		self.res = []
		def f(i,ds,n,arr):
		    if i>=n:
		        self.res.append(sum(ds[:]))
		        return
		    ds.append(arr[i])
            f(i+1,ds,n,arr)
            ds.pop()
            f(i+1,ds,n,arr)
            
        f(0,[],N,arr)
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