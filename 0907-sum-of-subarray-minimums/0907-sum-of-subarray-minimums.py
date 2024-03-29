# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         res = 0
        
#         for i in range(len(arr)):
#             for j in range(i,len(arr)):
#                 res += min(arr[i:j+1])
        
#         return res%(10**9+7)

#########################################################################


# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         MOD = 10 ** 9 + 7
#         stack = []
#         sum_of_minimums = 0;

#         for i in range(len(arr) + 1):
            
#             # when i reaches the array length, it is an indication that
#             # all the elements have been processed, and the remaining
#             # elements in the stack should now be popped out.

#             while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):

#                 # Notice the sign ">=", This ensures that no contribution
#                 # is counted twice. right_boundary takes equal or smaller 
#                 # elements into account while left_boundary takes only the
#                 # strictly smaller elements into account

#                 mid = stack.pop()
#                 left_boundary = -1 if not stack else stack[-1]
#                 right_boundary = i

#                 # count of subarrays where mid is the minimum element
#                 count = (mid - left_boundary) * (right_boundary - mid)
#                 sum_of_minimums += (count * arr[mid])

#             stack.append(i)
        
#         return sum_of_minimums % MOD

##########################################################################################


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # monotonic increasing stack
        stack = []

        # make a dp array of the same size as the input array
        dp = [0] * len(arr)

        # populate monotonically increasing stack
        for i in range(len(arr)):
            # before pushing an element, make sure all
            # larger and equal elements in the stack are
            # removed
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # calculate the sum of minimums of all subarrays
            # ending at index i
            if stack:
                previousSmaller = stack[-1]
                dp[i] = dp[previousSmaller] + (i - previousSmaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            stack.append(i)

        # add all the elements of dp to get the answer
        return sum(dp) % MOD
