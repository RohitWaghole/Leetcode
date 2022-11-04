class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [0]*len(pref)
        res[0] = pref[0]
        d = pref[0]
        for i in range(1,len(pref)):
            c = pref[i]^d
            d ^= c
            res[i] = c
        return res