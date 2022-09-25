class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        
        l = ''
        for i in word:
            if i.isdigit():
                l += i
            else:
                if l:
                    s.add(int(l))
                    l = ''
        if l:
            s.add(int(l))
        return len(s)