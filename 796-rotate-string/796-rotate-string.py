class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s)!=len(goal):
            return False
        
        if s==goal:
            return True
        
        for i in range(len(s)):
            x = s[i:] + s[:i]
            if x == goal:
                return True
            
        return False