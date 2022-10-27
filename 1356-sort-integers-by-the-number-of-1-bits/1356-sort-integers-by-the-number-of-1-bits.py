class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        l = []
        for i in sorted(arr):
            l.append([bin(i).count('1'),i])
        l.sort()
        return [i[1] for i in l]