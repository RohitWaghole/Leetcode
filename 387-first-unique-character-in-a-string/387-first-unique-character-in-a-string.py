class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        frequency = {}
        
        for ch in s:
            frequency[ch] = frequency.get(ch, 0)+1
        
        for ch, freq in frequency.items():
            
            if freq==1:
                return s.index(ch)
        
        return -1