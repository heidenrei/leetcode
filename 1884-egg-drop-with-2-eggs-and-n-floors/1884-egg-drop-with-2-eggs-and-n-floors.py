class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def go(moves, eggs):
            if not moves * eggs:
                return 0
            return go(moves-1, eggs-1) + go(moves-1, eggs) + 1
        
        l, r = 0, 10**4
        while l < r:
            m = l + r >> 1
            if go(m, 2) >= n:
                r = m
            else:
                l = m + 1
        return l