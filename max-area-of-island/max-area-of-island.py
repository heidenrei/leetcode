class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        d = defaultdict(int)
        DIRS = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def go(i, j, origin):
            grid[i][j] = 'x'
            d[origin] += 1
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 1:
                    go(ni, nj, origin)
                    
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    go(i, j, tuple([i, j]))
        
        best = 0
        
        for k, v in d.items():
            best = max(best, v)
            
        return best