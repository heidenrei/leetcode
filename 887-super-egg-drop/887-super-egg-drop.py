class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def go(moves, eggs): # returns most floors you can get to with n moves and m eggs
            if not moves * eggs:
                return 0
            return go(moves-1, eggs-1) + go(moves-1, eggs) + 1
        
        l, r = 0, 300
        while l < r:
            m = l + r >> 1
            if go(m, k) >= n:
                r = m
            else:
                l = m + 1
        return l
            