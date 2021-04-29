class Solution:
    def uniquePathsWithObstacles(self, A) -> int:
        R, C = len(A), len(A[0])
        
        @lru_cache(None)
        def go(i, j):
            if i >= R or j >= C or A[i][j] == 1:
                return 0

            if i == R-1 and j == C-1:
                return 1
            
            ways = 0
            ways += go(i+1, j)
            ways += go(i, j+1)
            
            return ways
        
        return go(0, 0)