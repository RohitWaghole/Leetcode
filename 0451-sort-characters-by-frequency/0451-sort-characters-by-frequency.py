class Solution:
    def frequencySort(self, s: str) -> str:
        
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
            
        templist = [[freq, char] for char, freq in hashmap.items()]
            
        templist.sort(reverse=True)
        return ''.join(j*i for i,j in templist)