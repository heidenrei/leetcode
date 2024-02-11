class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        @lru_cache(None)
        def go(lvl, r1, r2):
            if lvl == R:
                return 0
            
            best = 0
            for dr1 in [-1, 0, 1]:
                for dr2 in [-1, 0, 1]:
                    nr1, nr2 = r1 + dr1, r2 + dr2
                    if all([0 <= x < C for x in [nr1, nr2]]):
                    #if 0 <= nr1 < C and 0 <= nr2 < C:
                        cnt = grid[lvl][r1]
                        if r1 != r2:
                            cnt += grid[lvl][r2]
                            
                        best = max(best, cnt + go(lvl+1, nr1, nr2))
            return best
        
        return go(0, 0, C-1)