# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
        
#         d = {}
#         for i in arr:
#             if i in d:
#                 d[i]+=1
#             else:
#                 d[i]=1
#         return len(d.values())==len(set(d.values()))

#####################################################################################

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        seen = set()
        for frequency in Counter(arr).values():
            if frequency in seen:
                return False
            seen.add(frequency)
        return True