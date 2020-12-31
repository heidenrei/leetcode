class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9+7
        INF = float('inf')
        
        grid = [[x for x in y] for y in board]
        R, C = len(grid), len(grid[0])
        grid[0][0] = grid[R-1][C-1] = '0'
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] in 'SE':
                    grid[i][j] = 0
                elif grid[i][j] == 'X':
                    grid[i][j] = -INF
                else:
                    grid[i][j] = int(grid[i][j])
        
        dp = [[[0, 0] for x in range(R)] for y in range(C)]
        dp[R-1][C-1][1] = 1
        DIRS = [[1, 1], [0, 1], [1, 0]]
        
        for j in range(C-1, -1, -1):
            for i in range(R-1, -1, -1):
                if i != R-1 or j != C-1:
                    best = -INF
                    best_cnt = 0
                    for di, dj in DIRS:
                        ni, nj = i + di, j + dj
​
                        if 0 <= ni < R and 0 <= nj < C:
                            if best < dp[ni][nj][0] + grid[i][j]:
                                best = dp[ni][nj][0] + grid[i][j]
                                best_cnt = dp[ni][nj][1]
                            elif best == dp[ni][nj][0] + grid[i][j]:
                                best_cnt += dp[ni][nj][1]
                    dp[i][j] = [best, best_cnt]
        
        dp[0][0][1] = dp[0][0][1] % MOD
        dp[0][0][0] = dp[0][0][0] % MOD
        
        return dp[0][0] if not isinstance(dp[0][0][0], float) else [0, 0]
