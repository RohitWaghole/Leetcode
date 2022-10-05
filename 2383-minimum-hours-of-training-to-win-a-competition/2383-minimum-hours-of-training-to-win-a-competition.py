class Solution:
    def minNumberOfHours(self, inenergy: int, inexperience: int, energy: List[int], experience: List[int]) -> int:
        
        a = 0
        for i in energy:
            if inenergy<=i:
                a += i - inenergy + 1
                inenergy += i - inenergy + 1
            inenergy -= i
        
        b = 0
        for i in experience:
            if inexperience<=i:
                b += i - inexperience + 1
                inexperience += i - inexperience + 1
            inexperience += i
            
        return a+b