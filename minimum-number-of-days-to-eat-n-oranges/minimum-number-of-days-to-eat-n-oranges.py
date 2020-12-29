import sys
sys.setrecursionlimit(15000000)
​
class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def go(x):
            if x == 0:
                return 0
            best = float('inf')
            best = min(best, x%2 + go(x//2) + 1)
            best = min(best, x%3 + go(x//3) + 1)
            return best
        return go(n) - 1
