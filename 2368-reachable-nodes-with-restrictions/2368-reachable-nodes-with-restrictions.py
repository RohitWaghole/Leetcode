class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        self.result = 0
        restricted = set(restricted)
        
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [0]*n
        
        def dfs(node):
            if visited[node]==0:
                visited[node] = 1
                if node not in restricted:
                    self.result+=1
                    
                for it in graph[node]:
                    if visited[it]==0 and node not in restricted:
                        dfs(it)
                
                
        dfs(0)
        return self.result