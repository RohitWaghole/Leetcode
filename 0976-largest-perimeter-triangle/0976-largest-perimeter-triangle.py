class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # classification , strain gage, potentiometer problems 
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0