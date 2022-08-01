class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def go(i, j):
            if i == m - 1and j == n - 1:
                return 1
            ans = 0
            for di, dj in [[0,1],[1,0]]:
                ni, nj = di + i, dj + j
                if 0 <= ni < m and 0 <= nj < n:
                    ans += go(ni, nj)
                    
            return ans
        
        return go(0, 0)