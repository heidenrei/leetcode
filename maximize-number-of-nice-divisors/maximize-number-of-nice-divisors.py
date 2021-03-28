class Solution:
    def maxNiceDivisors(self, p: int) -> int:
        # are all nice divisors products of 6 or 10?
        # so all primes have to be either (2,3) or (2,5)?
        MOD = 10**9+7
        low_ans = [6, 9, 12]
        if p < 5:
            return p
        if p < 8:
            return low_ans[p-5]
        
        q, r = divmod(p-4, 3)
        return pow(3, q, MOD) * self.maxNiceDivisors(r+4) % MOD