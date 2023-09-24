class Solution:
    def champagneTower(self, poured: int, row: int, col: int) -> float:
        if poured == 0:
            return 0
        m = 200
        dp = [[0 for x in range(m)] for y in range(m)]
        if row == 0 and col == 0:
            return min(1, poured)
        dp[0][0] = poured - 1
        for i in range(1, m):
            for j in range(i+1):
                if j > 0:
                    dp[i][j] = dp[i-1][j-1]/2
                dp[i][j] += dp[i-1][j]/2
                if i == row and j == col:
                    return min(1, dp[i][j])
                dp[i][j] = max(0, dp[i][j]-1)