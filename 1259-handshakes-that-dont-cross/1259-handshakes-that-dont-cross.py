class Solution:
    def numberOfWays(self, n) -> int:
        n >>= 1
        MOD = 10**9+7
        @cache
        def f(x):
            if x <= 1:
                return 1
            ans = f(x-1) * x
            return ans % MOD

        def mi(x, y):
            y = pow(y, MOD-2, MOD)
            ans = x * y
            return ans % MOD
        
        return mi(f(2*n), (f(n+1) * f(n)))
        #return int((f(2*n) / (f(n+1) * f(n))))