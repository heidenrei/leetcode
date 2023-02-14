class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # count by centroid or centroid pair?
        ans = [0]*(n-1)
        dist = defaultdict(lambda: inf)
        for x in range(1, n+1):
            dist[(x, x)] = 0
        for x in edges:
            dist[tuple(x)] = 1
            dist[tuple(x[::-1])] = 1
        n += 1
        for j in range(1, n):
            for i in range(1, n):
                for k in range(1, n):
                    if i != j:
                        dist[(i, k)] = min(dist[(i, k)], dist[(i, j)] + dist[(j, k)])
        

        
        def ufind(x):
            if x not in s:
                s[x]
                p[x] = x
            if p[x] != x:
                p[x] = ufind(p[x])
            return p[x]
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            if s[ux] > s[uy]:
                uy, ux = uy, ux
            s[uy] += s[ux]
            p[ux] = uy
        
        
        for x in range(1, 2**n):
            nodes = []
            maxi = 0
            p = defaultdict(int)
            s = defaultdict(lambda: 1)
            for i in range(n):
                if x & (1<<i):
                    for y in nodes:
                        if dist[(i+1, y)] == 1:
                            uunion(i+1, y)
                        if dist[(i+1, y)] > maxi:
                            maxi = dist[(i+1, y)]
                    nodes.append(i+1)
            #print(maxi)
            if 0 < maxi < inf and s.values() and max(s.values()) == x.bit_count():
                #print(bin(x)[2:])
                ans[maxi-1] += 1
                
        return ans