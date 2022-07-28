# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s)==sorted(t)

#########################################################################################

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sd = Counter(s)
#         td = Counter(t)
#         return sd==td

##########################################################################################

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls,lt = [0]*26,[0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            ls[ord(s[i])-ord('a')]+=1
            lt[ord(t[i])-ord('a')]+=1
        for i in range(26):
            if ls[i]!=lt[i]:
                return False
        return True

##########################################################################################

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t): return False
#         l = [0]*256
#         for i in range(len(s)):
#             l[ord(s[i])]+=1
#             l[ord(t[i])]-=1
#         for i in l:
#             if i!=0:
#                 return False
#         return True
