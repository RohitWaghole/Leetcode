class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        fact = 1
        numbers = []
        for i in range(1,n):
            fact *= i
            numbers.append(i)
        numbers.append(n)
        
        k -= 1
        
        ans = ""
        
        while True:
            ans += str(numbers[k//fact])
            numbers.remove(numbers[k//fact])
            if len(numbers)==0:
                break
            k %= fact
            fact //= len(numbers)
        return ans