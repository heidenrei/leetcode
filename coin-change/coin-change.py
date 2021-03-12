class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        INF = math.inf
        dp = [[INF for x in range(amount+1)] for y in range(N+1)]
        for i in range(N+1):
            dp[i][0] = 0
        
        for i in range(1, N+1):
            for j in range(1, amount+1):
                if 0 <= j - coins[i-1] <= amount:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i-1]] + 1)
                dp[i][j] = min(dp[i][j], dp[i-1][j])
                
        return dp[-1][-1] if dp[-1][-1] != INF else -1