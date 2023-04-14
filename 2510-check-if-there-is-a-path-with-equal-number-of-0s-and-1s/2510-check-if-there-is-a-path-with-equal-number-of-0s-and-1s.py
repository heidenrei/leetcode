class Solution:
    def isThereAPath(self,A):
        R, C = len(A), len(A[0])
        
        for i in range(R):
            for j in range(C):
                if not A[i][j]:
                    A[i][j] -= 1
        
        DIRS = [[1,0,],[0,1]]
        @cache
        def go(i, j, d):
            if i == R -1 and j == C - 1:
                return not d
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if ni < R and nj < C:
                    if go(ni, nj, d + A[ni][nj]):
                        return True
            return False
        return go(0, 0, A[0][0])