class Solution:
    def longestIncreasingPath(self, A):
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,1],[0,-1],[-1,0]]
        
        @cache
        def go(i, j):
            ans = 0
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <=nj < C and A[ni][nj] > A[i][j]:
                    ans = max(ans, go(ni, nj)+1)
                    
            return ans
        
        best = 0
        for i in range(R):
            for j in range(C):
                tmp = go(i, j) + 1
                if tmp > best:best = tmp
                    
        return best