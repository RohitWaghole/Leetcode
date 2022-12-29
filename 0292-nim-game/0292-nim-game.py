class Solution:
    def canWinNim(self, n: int) -> bool:
        return 0 if n%4==0 else 1