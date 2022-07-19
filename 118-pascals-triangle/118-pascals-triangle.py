class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascalTriangle = [[1],[1,1]]
        for i in range(numRows-2):
            l = [1]
            for m in range(len(pascalTriangle[-1])-1):
                l.append(pascalTriangle[-1][m]+pascalTriangle[-1][m+1])
            l+=[1]
            pascalTriangle.append(l)
        return pascalTriangle[:numRows]