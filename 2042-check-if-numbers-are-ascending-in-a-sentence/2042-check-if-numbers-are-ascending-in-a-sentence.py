class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        c = ''
        mx = 0
        for i in s:
            if i.isdigit():
                c+=i
            else:
                if c!='':
                    x = int(c)
                    if x<=mx:
                        return False
                    mx = x
                    c = ''
        if c!=''and int(c)<=mx:
            return False
        return True