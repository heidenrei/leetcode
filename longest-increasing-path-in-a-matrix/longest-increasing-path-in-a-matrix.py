class Solution:
    def longestIncreasingPath(self, A) -> int:
        R, C = len(A), len(A[0])
        
        dp = [[1 for x in range(C)] for y in range(R)]
        
        DIRS = [[1, 0], [0,1], [-1,0], [0,-1]]
        
        def go(i, j):
            for di, dj in DIRS:
                ni, nj = i + di, j+dj
                if 0 <= ni < R and 0 <= nj < C and A[ni][nj] > A[i][j] and dp[i][j] + 1 > dp[ni][nj]:
                    dp[ni][nj] = dp[i][j] + 1
                    go(ni, nj)
        
        for i in range(R):
            for j in range(C):
                go(i, j)
        return max([max(x) for x in dp])