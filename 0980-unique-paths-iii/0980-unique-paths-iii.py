class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        N_rows = len(grid)
        N_cols = len(grid[0])
        
        sx = sy = None
        ex = ey = None
        spaces = 0
        
        for i in range(N_rows):
            for j in range(N_cols):
                if grid[i][j] == 1:
                    sx = i
                    sy = j
                    grid[i][j] = 0
                if grid[i][j] == 2:
                    ex = i
                    ey = j
                    grid[i][j] = 0
                if grid[i][j] == 0:
                    spaces += 1
                    
        paths = 0
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def backtrack(cx, cy, ex, ey, seen):
            if cx == ex and cy == ey and len(seen) == spaces:
                nonlocal paths
                paths += 1
                return
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N_rows and 0 <= ny < N_cols and grid[nx][ny] == 0 and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    backtrack(nx, ny, ex, ey, seen)
                    seen.remove((nx, ny))
                    
        seen = set()
        seen.add((sx, sy))
        backtrack(sx, sy, ex, ey, seen)
        
        
        
        return paths