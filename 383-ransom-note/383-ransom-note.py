class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = Counter(ransomNote)
        d2 = Counter(magazine)
        
        for key,val in d1.items():
            if d2.get(key,0) < val:
                return False
        return True