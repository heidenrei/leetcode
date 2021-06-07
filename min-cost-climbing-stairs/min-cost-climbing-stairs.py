class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        cost = cost + [0]
        dp = [math.inf for x in range(N+1)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[1], min(dp[0] + cost[0], dp[1] + cost[1]))
                
        for i in range(2, N+1):
            dp[i] = min(min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]), dp[i])
                
        return dp[-1]