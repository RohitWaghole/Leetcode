class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        i = len(arr)-2
        while i>=0 and arr[i]<=arr[i+1]:
            i -= 1
        if i>=0:
            mx = i+1
            for j in range(mx+1,len(arr)):
                if arr[mx] < arr[j] < arr[i]:
                    mx = j
            arr[mx], arr[i] = arr[i],arr[mx]
        return arr