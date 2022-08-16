class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if n==1 or source==destination:
            return True
            
        graph = [[] for i in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node):
            
            if visited[node]==0:
                if node==source:
                    self.a = 1
                elif node==destination:
                    self.b = 1
                    
                if self.a==1 and self.b==1:
                    return
                visited[node] = 1
                for it in graph[node]:
                    dfs(it)
        
        
        visited = [0]*n
        for i in range(n):
            self.a,self.b = 0,0
            if visited[i]==0:
                dfs(i)
            if self.a==1 and self.b==1:
                return True
        
        
        
        
        
        return False