class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0 for x in range(n)] for y in range(m)] for z in range(maxMove+1)]
        dp[0][startRow][startColumn] = 1
        ans = 0
        
        DIRS = [[1,0], [0,1], [-1,0], [0,-1]]
        
        for move in range(maxMove):
            for x in range(m):
                for y in range(n):
                    curr = dp[move][x][y]
                    if curr > 0:
                        for dx, dy in DIRS:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n:
                                dp[move+1][nx][ny] += curr
                            else:
                                ans += curr
                                    
        return ans % MOD