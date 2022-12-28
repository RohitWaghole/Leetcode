# class Solution:
#     def minStoneSum(self, piles: List[int], k: int) -> int:
#         piles.sort(reverse=True)
#         while k:
#             piles[0] = piles[0]//2 + piles[0]%2
#             piles.sort(reverse=True)
#             k -= 1
#         return sum(piles)

#################################################################################

# class Solution:
#     def minStoneSum(self, piles: List[int], k: int) -> int:
#         piles.sort()
#         while k:
#             ele = piles[-1]//2 + piles[-1]%2
#             piles.pop()
#             bisect.insort_left(piles, ele)
#             k -= 1
#         return sum(piles)

#################################################################################

import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))
        
        return -sum(heap)