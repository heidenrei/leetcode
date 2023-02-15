class Solution:
    def numIslands2(self, R: int, C: int, positions: List[List[int]]) -> List[int]:
        DIRS = [[1,0],[0,1],[0,-1],[-1,0]]
        s = defaultdict(lambda: 1)
        p = defaultdict(int)
        
        def ufind(x):
            if x not in p:
                s[x]
                p[x] = x
            if p[x] != x:
                p[x] = ufind(p[x])
            return p[x]
        
        def uunion(x, y):
            ux, uy = ufind(x), ufind(y)
            if ux == uy:
                return
            if s[ux] > s[uy]:
                ux, uy = uy, ux
            
            s[uy] += s[ux]
            p[ux] = uy
            
        islands = 0
        ans = []
        for i, j in positions:
            if (i, j) in p:
                ans.append(islands)
                continue
            neighbors = []
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) in p:
                    neighbors.append((ni, nj))
            islands += 1                    
            if not neighbors:
                ufind((i, j))
            else:
                neighbors.append((i, j))
                for ti in range(len(neighbors)):
                    for tj in range(ti):
                        if ufind(neighbors[ti]) != ufind(neighbors[tj]):
                            islands -= 1
                            uunion(neighbors[ti], neighbors[tj])
                            
            ans.append(islands)
            
        return ans
                            