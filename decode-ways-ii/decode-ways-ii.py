class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        MOD = 10**9+7
        dp = [0 for x in range(N+1)]
        dp[0] = 1
        
        for idx in range(N):
            curr = s[idx]
            
            if curr == '0':
                if idx == 0 or s[idx-1] not in '12*':
                    return 0
                dp[idx+1] = dp[idx]
                continue
            
            # 1 digit
            if curr == '*':
                if idx+1 < N:
                    if s[idx+1] == '0':
                        dp[idx+1] = 2 * dp[idx]
                        continue
                dp[idx+1] += 9 * dp[idx]
            else:
                dp[idx+1] += dp[idx]
                
            # 2 digit
            if idx - 1 >= 0:
                prev = s[idx-1]
                if prev == '0':
                    continue
                
                if idx + 1 < N:
                    if s[idx+1] == '0':
                        dp[idx+1] = dp[idx]
                        continue
                
                if prev == '1':
                    if curr == '*':
                        dp[idx+1] += 9 * dp[idx-1]
                    else:
                        dp[idx+1] += dp[idx-1]
                if prev == '2':
                    if curr == '*':
                        dp[idx+1] += 6 * dp[idx-1]
                    elif curr <= '6':
                        dp[idx+1] += dp[idx-1]
                if prev == '*':
                    if curr == '*':
                        dp[idx+1] += 15 * dp[idx-1]
                    else:
                        if curr <= '6':
                            dp[idx+1] +=  dp[idx-1]
                        dp[idx+1] += dp[idx-1]
                dp[idx+1] %= MOD
                        
        return dp[-1]