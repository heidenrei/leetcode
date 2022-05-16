class Solution:
    def cherryPickup(self, A):
        R, C = len(A), len(A[0])
        if R == 1 and C == 1:
            if A[0][0] == 1:
                return 1
            else:
                return 0
        DIRS = [[1,0], [0,1]]
        @cache
        def go(i1, j1, i2, j2):
            if i1 == R-1 and j1 == C-1 and i2 == R-1 and j2 == C-1:
                return 0
            ans = -inf
            for di1, dj1 in DIRS:
                ni1, nj1 = di1 + i1, dj1 + j1
                if 0 <= ni1 < R and 0 <= nj1 < C and A[ni1][nj1] != -1:
                    for di2, dj2 in DIRS:
                        ni2, nj2 = di2 + i2, dj2 + j2
                        if 0 <= ni2 < R and 0 <= nj2 < C and A[ni2][nj2] != -1:
                            tmp = go(ni1, nj1, ni2, nj2)
                            if ni1 != ni2 or nj1 != nj2:
                                tmp += A[ni1][nj1] + A[ni2][nj2]
                            else:
                                tmp += A[ni1][nj1]
                            if tmp > ans:
                                ans = tmp
            return ans
        ans = go(*[0,0,0,0]) + int(A[0][0] == 1) 
        return max(ans, 0)