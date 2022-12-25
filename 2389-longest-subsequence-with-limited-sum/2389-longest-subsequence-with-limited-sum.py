# class Solution:
#     def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         nums.sort()
#         ans = []
#         for q in queries:
#             c = 0
#             for i in nums:
#                 if q>=i:
#                     q -= i
#                     c += 1
#                 else:
#                     break
#             ans.append(c)
#         return ans

##############################################################################################

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Get the prefix sum array of the sorted 'nums'.
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        answer = []
        
        # For each query, find its insertion index to the prefix sum array.
        for query in queries:
            index = bisect.bisect_right(nums, query)
            answer.append(index)
            
        return answer