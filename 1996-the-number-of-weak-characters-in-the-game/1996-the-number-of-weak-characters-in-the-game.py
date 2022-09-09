class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x: (-x[0],x[1]))
        result = 0
        curr_max = 0
        for a,b in properties:
            if b<curr_max:
                result += 1
            else:
                curr_max = b
        return result