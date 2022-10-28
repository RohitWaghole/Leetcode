class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        t = [[''.join(sorted(v)),i] for i,v in enumerate(strs)]
        t.sort()
        temp = []
        tp = []
        result = []
        for i in range(len(t)):
            if temp==[]:
                temp.append(t[i])
                tp.append(strs[t[i][1]])
            elif temp[-1][0]==t[i][0]:
                temp.append(t[i])
                tp.append(strs[t[i][1]])
            else:
                result.append(tp)
                tp = [strs[t[i][1]]]
                temp = [t[i]]
        if temp!=[]:
            result.append(tp)
        return result