class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        frequency = {}
        
        for ch in s:
            frequency[ch] = frequency.get(ch, 0)+1
        
        for ind, ch in enumerate(s):
            if frequency[ch]==1:
                return ind
        
        return -1

        