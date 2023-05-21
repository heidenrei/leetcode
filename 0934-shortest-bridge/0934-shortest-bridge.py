class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        seen = set()
        
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def go(i, j):
            grid[i][j] = 'x'
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C:
                    if grid[ni][nj] == 1:
                        go(ni, nj)
        
        found_first_island = False
        q = deque()

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    if not found_first_island:
                        go(i, j)
                        found_first_island = True
                    else:
                        q.append([i, j]) 
        
        level = -1
        
        while q:
            tmp = []
            while q:
                i, j = q.popleft()
                if grid[i][j] == 'x':
                    return level
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C:
                        coords = tuple([ni, nj])
                        if coords not in seen:
                            seen.add(coords)
                            tmp.append(coords)
                            
            level += 1
            q.extend(tmp)
                 
                
        return -1