class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def go(i, last):
            if i == n:
                return 1
            if i < 1 and not last:
                return k * go(i+1, False)
            elif not last:
                return (k-1) * go(i+1, False) + go(i+1, True)
            elif last:
                return (k-1) * go(i+1, False)
            
        return go(0,0)