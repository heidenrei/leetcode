class Solution:
    def hasValidPath(self, A):
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,1]]
        if A[0][0] == ')':
            return False
        @cache
        def go(i, j, opn):
            if i == R-1 and j == C-1:
                return True if opn == 0 else False
            ans = False
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C:
                    if A[ni][nj] == ')' and opn > 0 and go(ni, nj, opn-1):
                        ans = True
                    if A[ni][nj] == '(' and go(ni, nj, opn+1):
                        ans = True
                        
            return ans
        
        return go(0,0,1)