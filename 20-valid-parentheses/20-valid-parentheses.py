class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        d = {')':'(', '}':'{', ']':'['}
        
        for i in s:
            if i in d.values():
                stack.append(i)
            else:
                if stack==[] or d[i] != stack.pop():
                    return False
        return stack == []