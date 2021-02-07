class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        INF = float('inf')
        dp = [INF for x in range(N)]
        curr = INF
        for i in range(N):
            if s[i] == c:
                curr = 0
            else:
                curr += 1
            dp[i] = min(dp[i], curr)
        
        curr = INF
        for i in range(N)[::-1]:
            if s[i] == c:
                curr = 0
            else:
                curr += 1
            dp[i] = min(dp[i], curr)
            
        return dp