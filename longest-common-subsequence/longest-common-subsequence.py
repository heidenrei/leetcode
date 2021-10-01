class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        Na = len(a)
        Nb = len(b)

        dp = [[0 for _ in range(Na+1)] for _ in range(Nb+1)]
        for i in range(1, Nb+1):
            for j in range(1, Na+1):
                if b[i-1] == a[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lcs = max(max(x) for x in dp)
        
        return lcs