class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        @cache
        def go(i, sumi):
            if i == n:
                return sumi == target
            if sumi > target:
                return 0
            ans = 0
            for ds in range(1, k+1):
                ans += go(i+1, sumi+ds)
                ans %= MOD
                
            return ans
        return go(0, 0)