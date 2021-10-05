class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return [0,1,2][n]
        
        n += 1
        
        dp = [0]*n
        dp[:3] = [0,1,2]
        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2]
                
        return dp[-1]