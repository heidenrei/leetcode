class Solution:
    def numTrees(self, n: int) -> int:
        
        @functools.lru_cache(n)
        def go(rem):
            if rem == 0:
                return 1
            return sum(go(x) * go(rem-x-1) for x in range(rem))
        
        return go(n)