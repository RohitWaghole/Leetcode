class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        text = text.split()
        count = 0
        
        brokenLetters = list(set(brokenLetters))
        
        for word in text:
            
            for letter in brokenLetters:
                if letter in word:
                    break
            else:
                count += 1
                
        return count