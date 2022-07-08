class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        for element in nums1:
            maximum = -1
            flag = 0
            for value in nums2:
                if element==value:
                    flag = 1
                if flag and value>element:
                    maximum = value
                    break
            result.append(maximum)
        return result