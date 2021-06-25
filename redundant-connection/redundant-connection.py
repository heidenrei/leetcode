class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edges = [[x-1, y-1] for x, y in edges]
        ans = -1
        N = max([max(x) for x in edges])+1
        def ufind(x):
            if parent[x] != x:
                return ufind(parent[x])
            return parent[x]
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            
            if parent_size[uy] >= parent_size[ux]:
                parent[ux] = uy
                parent_size[uy] = parent_size[uy] + parent_size[ux]
            else:
                parent[uy] = ux
                parent_size[ux] = parent_size[uy] + parent_size[ux]
        
        for i in range(len(edges))[::-1]:
            parent = [x for x in range(N)]
            parent_size = [1 for x in range(N)]

            for x, y in edges:
                if [x,y] != edges[i]:
                    if ufind(x) != ufind(y):
                        uunion(x,y)
                        if parent_size[ufind(y)] == N or parent_size[ufind(x)] == N:
                            ans = edges[i]
                        
                            return [ans[0]+1, ans[1]+1]