class Solution:
    def countTexts(self, s: str) -> int:
        MOD = 10**9+7
        s = '0' + s
        N = len(s)
        dp = [0]*N
        dp[0] = 1
        
        for i in range(1, N):
            # if s[i] != s[i-1]:
            #     dp[i] = dp[i-1]
            if s[i] in '79':
                for j in range(1,5):
                    dp[i] += dp[i-j]
                    dp[i] %= MOD
                    if s[i] != s[i-j]:
                        break

            else:
                for j in range(1, 4):
                    dp[i] += dp[i-j]
                    dp[i] %= MOD
                    if s[i] != s[i-j]:
                        break
                
        return dp[-1]