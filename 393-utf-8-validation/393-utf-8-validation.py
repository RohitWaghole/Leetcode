class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        i = 0
        while i<len(data):
            
            t = bin(data[i])[2:]
            t = '0'*(8-len(t)) + t
            if t.startswith('0'):
                i += 1
            elif t.startswith('110'):
                i+=1
                t = bin(data[i])[2:]
                t = '0'*(8-len(t)) + t
                if t.startswith('10'):
                    i += 1
                else:
                    return False
            elif t.startswith('1110'):
                i += 1
                for m in range(2):
                    if i==len(data):
                        return False
                    t = bin(data[i])[2:]
                    t = '0'*(8-len(t)) + t
                    if t.startswith('10'):
                        i += 1
                    else:
                        return False
            elif t.startswith('11110'):
                i += 1
                for m in range(3):
                    if i==len(data):
                        return False
                    t = bin(data[i])[2:]
                    t = '0'*(8-len(t)) + t
                    if t.startswith('10'):
                        i += 1
                    else:
                        return False
            else:
                return False
            
        return True