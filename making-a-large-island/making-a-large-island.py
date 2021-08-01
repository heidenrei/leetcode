class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        DIRS = [[1,0], [0,1], [-1,0], [0,-1]]
        
        p = defaultdict(tuple)
        s = defaultdict(lambda: 1)
        
        best = 0
        
        def ufind(x):
            if p[x] != x:
                p[x] = ufind(p[x])
            return p[x]
        
        def uunion(x, y): 
            ux = ufind(x)
            uy = ufind(y)
            
            if s[uy] > s[ux]:
                ux, uy = uy, ux
                
            p[uy] = ux
            s[ux] += s[uy]
        
        ans = 0
        
        for i in range(R):
            for j in range(C):
                p[tuple([i, j])] = tuple([i, j])
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    for di, dj in DIRS:
                        ni, nj = di + i, dj + j
                        if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 1 and ufind(tuple([ni, nj])) != ufind(tuple([i, j])):
                            uunion(tuple([i, j]), tuple([ni, nj]))
                            
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    neighbors = set()
                    for di, dj in DIRS:
                        ni, nj = di + i, dj + j
                        if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 1:
                            neighbors.add(ufind(tuple([ni, nj])))
                            
                    neighbors = sorted([s[x] for x in neighbors], reverse=True)
                    if neighbors.__len__() >= 2:
                        best = max(best, sum(neighbors))
        
        if s.values():
            max_val = max(x for x in s.values())
            if max_val < R*C:
                max_val += 1
        else:
            max_val = 0
        return max(best + 1, max_val)