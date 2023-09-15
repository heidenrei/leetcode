class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        parent = [x for x in range(N)]
        total = 0
        
        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            parent[uy] = ux
            
        def cost(a, b):
            return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])
        
        for i in range(N):
            for j in range(i):
                edges.append((cost(i, j), i, j))
                
        edges.sort()
        
        for cost, v1, v2 in edges:
            if ufind(v1) != ufind(v2):
                total += cost
                uunion(v1, v2)
                
        return total