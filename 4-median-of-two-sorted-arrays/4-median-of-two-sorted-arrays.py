# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
#         nums = sorted(nums1+nums2)
#         if len(nums)%2==0:
#             return ((nums[len(nums)//2]+nums[len(nums)//2 -1])/2)
#         return nums[len(nums)//2]

###############################################################################################################

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = []
        
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                n.append(nums1[i])
                i+=1
            else:
                n.append(nums2[j])
                j+=1
        while i<len(nums1):
            n.append(nums1[i])
            i+=1
        while j<len(nums2):
            n.append(nums2[j])
            j+=1
        
        if len(n)%2==0:
            return (n[len(n)//2]+n[len(n)//2-1])/2
        return n[len(n)//2]