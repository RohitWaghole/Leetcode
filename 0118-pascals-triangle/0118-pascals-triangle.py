# T.C. -> ~O(N^2)
# S.C. -> O(N)

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        p = [[1]]
        for i in range(n-1):
            temp = [1]
            for j in range(len(p[-1])-1):
                temp.append(p[-1][j]+p[-1][j+1])
            temp.append(1)
            p.append(temp)
        return p