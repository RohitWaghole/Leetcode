# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
        
#         result = []
#         for i in range(len(nums)):
#             c = 0
#             for j in range(i+1,len(nums)):
#                 if nums[i]>nums[j]:
#                     c+=1
#             result.append(c)
#         return result

#########################################################################################

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller