class Solution:
    def countArrangement(self, n: int) -> int:
        # bitmask dp
        
        @lru_cache(None)
        def go(i, bm):
            if i == n + 1:
                return 1
            
            total = 0
            for num in range(1, n+1):
                if (bm & (1 << (num-1))) == 0 and (i % num == 0 or num % i == 0):
                    total += go(i+1, bm ^ (1 << (num-1)))
            
            return total
        
        return go(1, 0)
