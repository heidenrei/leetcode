class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        @cache
        def go(i, j):
            if i == R -1 and j == C - 1:
                return 1
            ans = 0
            if i + 1 < R and A[i+1][j] != 1:
                ans += go(i+1, j)
            if j + 1 < C and A[i][j+1] != 1:
                ans += go(i, j+1)
            return ans
        
        return go(0, 0) if A[0][0] == 0 else 0