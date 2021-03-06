#User function Template for python3

# def isSubset( a1, a2, n, m):
    
#     for i in range(m):
#         element = a2[i]
#         flag = 1
#         for j in range(n):
#             if a1[j]==element:
#                 flag = 0
#                 break
#         if flag:
#             return "No"
#     return "Yes"
    
# ############################################################################

# def isSubset( a1, a2, n, m):
#     a1.sort()
#     for i in a2:
#         if not binarySearch(a1,i):
#             return "No"
#     return "Yes"
    
# def binarySearch(lst,element):
    
#     start,end = 0, len(lst)-1
#     while start<=end:
#         mid = start+(end-start)//2
#         if lst[mid]==element:
#             return 1
#         if lst[mid]>element:
#             end = mid-1
#         else:
#             start = mid+1
#     return 0

####################################################################################

# def isSubset( a1, a2, n, m):
#     a1.sort()
#     a2.sort()
#     if n<m:
#         return "No"
#     i,j=0,0
#     while i<n and j<m:
#         if a1[i]<a2[j]:
#             i+=1
#         if a1[i]==a2[j]:
#             i+=1
#             j+=1
#         elif a1[i]>a2[j]:
#             return "No"
#     if j==m:
#         return "Yes"
#     return "No"

#################################################################################

def isSubset( a1, a2, n, m):
    
    hashset = set()
    for i in range(n):
        hashset.add(a1[i])
    
    for i in range(m):
        if a2[i] in hashset:
            continue
        return "No"
    return "Yes"
# ##################################################################################

# def isSubset( a1, a2, n, m):  
    
#     d1 = {}
#     d2 = {}
#     for i in a1:
#         if i in d1:
#             d1[i]+=1
#         else:
#             d1[i]=1
#     for i in a2:
#         if i in d2:
#             d2[i]+=1
#         else:
#             d2[i]=1
            
#     for key,val in d2.items():
#         c = d1.get(key,0)
#         if c<val:
#             return "No"
#     return "Yes"
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends