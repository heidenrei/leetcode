class Solution:
    def minArea(self, A, i, j):
        R, C = len(A), len(A[0])
        jmin, jmax, imin, imax = j, j, i, i
        DIRS = [[1,0],[0,1],[-1,0],[0,-1]]
        seen = set()
        seen.add((i, j))
        
        def go(i, j):
            nonlocal jmin, jmax, imin, imax
            jmin = min(j, jmin); jmax = max(j, jmax); imin = min(i, imin); imax = max(i, imax)
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen and A[ni][nj] == '1':
                    seen.add((ni, nj))
                    go(ni, nj)
        go(i, j)
        #print(jmin, jmax, imin, imax)
        return (imax-imin+1) * (jmax-jmin+1)