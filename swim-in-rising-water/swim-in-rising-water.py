class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        DIRS = [[0,1], [1,0],[-1,0], [0,-1]]
        max_val = max([max(x) for x in grid])
        
        def is_good(maxi):
            found_ans = False
            seen = set()
            seen.add(tuple([0, 0]))
            
            def go(i, j, maxi):
                if i == R - 1 and j == C - 1:
                    nonlocal found_ans
                    found_ans = True
                    return
                for di, dj in DIRS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] <= maxi and tuple([ni, nj]) not in seen:
                        seen.add(tuple([ni, nj]))
                        go(ni, nj, maxi)
                        
            go(0, 0, maxi)
            
            return found_ans
        
        l = grid[0][0]
        r = max_val
        
        while l < r:
            m = l + r >> 1
            if not is_good(m):
                l = m + 1
            else:
                r = m
                
        return l