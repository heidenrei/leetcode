class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        s = [int(x) for x in s]
        N, M = len(s), len(str(k))
        MOD = 10**9+7
    
        dp = [0 for x in range(N+1)]
        dp[0] = 1
        for i in range(N):
            if not dp[i]:
                continue
            curr = 0
            j = i+1
            while j <= N:
                curr = curr*10 + s[j-1]
                if curr > k:
                    break
                if j == N or s[j]:
                    dp[j] += dp[i]
                    dp[j] %= MOD
                j += 1
        #print(dp)
        return dp[-1]