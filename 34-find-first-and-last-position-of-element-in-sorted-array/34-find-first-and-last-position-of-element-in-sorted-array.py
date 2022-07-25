# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         first = -1
#         last = -1
#         for i in range(len(nums)):
#             if nums[i] == target and first==-1:
#                 first = i
#                 last = i
#             elif nums[i]==target:
#                 last = i
#         return [first,last]

####################################################################################################

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l = self.searchLeft(nums,target)
        r = self.searchRight(nums,target)
        
        return [l,r] if l<=r else [-1,-1]
    
    def searchLeft(self,a,x):
        lo,hi = 0,len(a)-1
        while lo<=hi:
            m = (lo+hi)//2
            if x>a[m]:
                lo=m+1
            else:
                hi=m-1
        return lo
    
    def searchRight(self,a,x):
        lo,hi = 0,len(a)-1
        while lo<=hi:
            m = (lo+hi)//2
            if x>=a[m]:
                lo=m+1
            else:
                hi=m-1
        return hi