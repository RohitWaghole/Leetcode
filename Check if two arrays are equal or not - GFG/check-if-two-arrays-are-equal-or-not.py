#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,a,b,N):
        
        d = {}
        if len(a)!=len(b):
            return False
        # for i in a:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # for i in b:
        #     if d[i]==0:
        #         return False
        #     d[i]-=1
        # return True
        
        
        count = defaultdict(int)
        for i in a:
            count[i] += 1
        for i in b:
            if (count[i] == 0):
                return False
      
            # If element is found, decrement
            # its value in the dictionary
            else:
                count[i] -= 1
      
        # Return true if both arr1 and
        # arr2 are equal
        return True
        
        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends