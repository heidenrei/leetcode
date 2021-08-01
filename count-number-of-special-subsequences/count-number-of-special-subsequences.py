class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [1, 0, 0, 0]
        for x in nums:
            dp[x+1] += dp[x+1] + dp[x]
            
        return dp[-1] % (10**9+7)