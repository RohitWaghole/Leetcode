# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         l = []
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 l.append(matrix[i][j])
#         l.sort()
#         return l[k-1]

##############################################################################################

'''
The property of HEAP data structure in Python is that each time the smallest of heap element is popped(min heap). Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element also returns the smallest element each time.
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        maxHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                heappush(maxHeap,-matrix[i][j]) # adds elements in the list
                
                if len(maxHeap)>k:
                    heappop(maxHeap) # pops the smallest element from the list regardless of its position
                    
        return -heappop(maxHeap)