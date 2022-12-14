class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        dp = [0]*N

        if N < 3:
            return max(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        
        for i in range(2, N):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                
        return max(dp)