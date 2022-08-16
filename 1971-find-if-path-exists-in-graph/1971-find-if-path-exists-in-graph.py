class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node):
            
            if visited[node]==0:
                
                if node==destination:
                    return True
                    
                visited[node] = 1
                for it in graph[node]:
                    if dfs(it):
                        return True
            return False
        
        
        visited = [0]*n
        return dfs(source)