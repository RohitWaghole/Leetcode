#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        hash_map = {}
        max_length = 0
        curr_sum = 0
        
        for index,value in enumerate(arr):
            
            curr_sum += value
            if curr_sum == 0:
                max_length = index+1
            
            if value==0 and max_length == 0:
                max_length = 1
                
            if curr_sum in hash_map:
                
                max_length = max(max_length, index - hash_map[curr_sum])
                
            else:
                
                hash_map[curr_sum] = index
                
        return max_length
        
        
        
        
        
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