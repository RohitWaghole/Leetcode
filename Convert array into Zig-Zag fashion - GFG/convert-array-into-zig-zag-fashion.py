#User function Template for python3
class Solution:

	def zigZag(self,a, n):
		# code here
		f = 1
		for i in range(n-1):
            if f:
                if a[i]>a[i+1]:
                    a[i],a[i+1]=a[i+1],a[i]
                f=0
            else:
                if a[i]<a[i+1]:
                    a[i],a[i+1]=a[i+1],a[i]
                f=1
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends