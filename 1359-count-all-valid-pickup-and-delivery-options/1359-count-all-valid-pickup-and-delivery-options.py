class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def go(x):
            if x == 1:
                return 1
            else:
                return (go(x-1) * x * (2 * x - 1)) % MOD
            
        return go(n)