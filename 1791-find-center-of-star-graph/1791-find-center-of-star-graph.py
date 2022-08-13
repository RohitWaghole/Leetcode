class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        mx,res = 0,-1
        graph = [0]*(len(edges)+2)
        for u,v in edges:
            graph[u]+=1
            graph[v]+=1
        for i in range(len(graph)):
            if graph[i]>mx:
                mx = graph[i]
                res = i
        return res