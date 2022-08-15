class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        
        s = s[::-1]
        ans = 0
        i = 0
        while i<len(s):
            
            if s[i]=='I':
                ans+=d[s[i]]
                i+=1
            elif i+1<len(s) and s[i]!=s[i+1] and (s[i+1]+s[i]) in d:
                ans += d[s[i+1]+s[i]]
                i+=2
            else:
                ans+=d[s[i]]
                i+=1
        return ans