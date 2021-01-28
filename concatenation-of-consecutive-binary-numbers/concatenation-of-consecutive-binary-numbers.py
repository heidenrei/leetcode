class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9+7
        ans = 0
        l = 0
        
        for x in range(1, n+1):
            if x & (-x) == x: l += 1
            ans = (ans * (1 << l) + x) % MOD
                
        return ans