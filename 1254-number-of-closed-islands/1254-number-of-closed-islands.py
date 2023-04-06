class Solution:
    def closedIsland(self, A) -> int:
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,1],[-1,0],[0,-1]]
        q = []
        for i in range(R):
            if not A[i][0]:
                q.append([i, 0])
                A[i][0] = 1
            if not A[i][-1]:
                q.append([i, C-1])
                A[i][-1] = 1
        for j in range(C):
            if not A[0][j]:
                q.append([0, j])
                A[0][j] = 1
            if not A[R-1][j]:
                q.append([R-1, j])
                A[-1][j] = 1
        
        def go(i, j):
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and not A[ni][nj]:
                    A[ni][nj] = 1
                    go(ni, nj)
                    
        for i, j in q:
            go(i, j)
        
        
        ans = 0
        for i in range(R):
            for j in range(C):
                if not A[i][j]:
                    go(i, j)
                    ans += 1
        return ans
        