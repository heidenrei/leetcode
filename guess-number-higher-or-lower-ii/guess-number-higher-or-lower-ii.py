class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def go(low, high):
            if low >= high:
                return 0
            best = math.inf
            for x in range(low, high):
                best = min(best, x + max(go(x+1, high), go(low, x-1)))
            return best
        
        return go(1, n)