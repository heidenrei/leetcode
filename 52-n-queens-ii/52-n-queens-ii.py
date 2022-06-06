class Solution:
    def totalNQueens(self, n: int) -> int:
        def get_d1(i, j):
            di, dj = -1, -1
            while 0 <= i and 0 <= j:
                i, j = i + di, j + dj
            return i, j
        
        def get_d2(i, j):
            di, dj = -1, 1
            while 0 <= i and j < n:
                i, j = i + di, j + dj
            return i, j
        @cache
        def go(i, jbm, d1, d2):
            if jbm == 2**n-1:
                return 1
            ans = 0
            for j in range(n):
                if not jbm & (1<<j):
                    td1 = get_d1(i, j)
                    td2 = get_d2(i, j)
                    if td1 not in d1 and td2 not in d2:
                        nd1 = tuple(list(d1) + [td1])
                        nd2 = tuple(list(d2) + [td2])
                        ans += go(i+1, jbm | (1<<j), nd1, nd2)
                        
            return ans
        
        return go(0, 0, tuple(), tuple())
            