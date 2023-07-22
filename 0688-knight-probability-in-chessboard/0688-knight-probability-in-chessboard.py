class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        DIRS = []
        for x in [1,-1,-2,2]:
            for y in [1,-1,-2,2]:
                if abs(x) + abs(y) == 3:
                    DIRS.append([x, y])
        @cache
        def go(i, j, rem):
            if rem == 0:
                return 1
            ans = 0
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < n and 0 <= nj < n:
                    ans += go(ni, nj, rem-1)
            return ans
        
        return go(row, column, k)/pow(8, k)