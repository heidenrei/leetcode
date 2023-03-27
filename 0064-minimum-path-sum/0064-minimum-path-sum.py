class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        @cache
        def go(i, j):
            if i == R - 1 and j == C - 1:
                return A[i][j]
            if i == R or j == C:
                return inf
            return min(go(i+1,j), go(i, j+1)) + A[i][j]
        
        return go(0, 0)
            