class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ''
        for i in s:
            c = i.lower()
            if c in ['a','e','i','o','u']:
                vowels = i+vowels
        res = ''
        t = 0
        for i in s:
            c = i.lower()
            if c in ['a','e','i','o','u']:
                res += vowels[t]
                t += 1
            else:
                res += i
        return res