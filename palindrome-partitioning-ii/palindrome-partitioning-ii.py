class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        
        dp = [x for x in range(N+1)]
        
        #@cache
        def is_pal(x):
            return x == x[::-1]
        
        for j in range(N+1):
            for i in range(j):
                if is_pal(s[i:j]):
                    if dp[i] + 1 < dp[j]:
                        dp[j] = dp[i]+1
        
        return dp[-1] - 1
