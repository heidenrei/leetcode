class Solution:
    def uniquePaths(self, R: int, C: int) -> int:
        @cache
        def go(i, j):
            if i == R-1 and j == C-1:
                return 1
            if i == R or j == C:
                return 0
            return go(i+1, j) + go(i, j+1)
        return go(0,0)