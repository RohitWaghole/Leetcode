class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        res = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        a = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        for i in letters:
            if i!= target and i>target and i<res:
                res = i
        return res if res!=a else letters[0]