class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for x in nums:
            idx = bisect_left(dp, x)
            if idx < len(dp):
                dp[idx] = x
            else:
                dp.append(x)
                
        return len(dp)