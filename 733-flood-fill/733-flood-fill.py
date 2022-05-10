class Solution:
    def floodFill(self, A, i, j, c):
        R, C = len(A), len(A[0])
        seen = set()
        DIRS = [[1, 0], [0,1], [0,-1], [-1,0]]
        def dfs(i, j, oc):
            A[i][j] = c
            seen.add((i, j))
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and A[ni][nj] == oc and (ni, nj) not in seen:
                    dfs(ni, nj, oc)
                    
        dfs(i, j, A[i][j])
        return A
        