class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
#         @cache
#         def go(i, a, l):
#             if i == n:
#                 return 1
#             ans = 0
#             ans += go(i+1, a, 0)
#             ans %= MOD
#             if not a:
#                 ans += go(i+1, 1, 0)
#                 ans %= MOD
#             if l < 2:
#                 ans += go(i+1, a, l+1)
#                 ans %= MOD
                
#             return ans
        
#         return go(0, 0, 0)
    
        dp = [[[0 for w in range(3)] for y in range(2)] for x in range(n+1)]
        dp[0][0][0] = 1
        for i in range(1, n+1):
            for a in range(2):
                for l in range(3):
                    dp[i][a][0] += dp[i-1][a][l] % MOD
                    #dp[i][a][0] %= MOD
                    if a > 0:
                        dp[i][a][0] += dp[i-1][a-1][l] % MOD
                    #dp[i][a][0] %= MOD
                    if l > 0:
                        dp[i][a][l] += dp[i-1][a][l-1] % MOD
                        #dp[i][a][l] %= MOD
                    
#         ans = 0
#         for a in range(2):
#             for l in range(3):
#                 ans += dp[-1][a][l] % MOD
                
        #return ans
        return sum(sum(x) % MOD for x in dp[-1]) %MOD