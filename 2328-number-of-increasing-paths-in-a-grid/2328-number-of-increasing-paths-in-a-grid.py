class Solution:
    def countPaths(self, A: List[List[int]]) -> int:
        DIRS = [[1,0],[0,1],[0,-1],[-1,0]]
        R, C = len(A), len(A[0])
        MOD = 10**9+7
        @cache
        def go(i, j):
            ans = 1
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and A[ni][nj] > A[i][j]:
                    ans += go(ni, nj)
                    ans %= MOD
            return ans
        ans = 0
        for i in range(R):
            for j in range(C):
                ans += go(i, j)
                ans %= MOD
                
        return ans