class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        @cache
        def go(i, j):
            if i == R:
                return 0
            cands = [go(i+1, j) + A[i][j]]
            if j > 0:
                cands.append(go(i+1, j-1) + A[i][j-1])
            if j < C-1:
                cands.append(go(i+1, j+1) + A[i][j+1])
            return min(cands)
        
        return min([go(0, j) for j in range(C)])