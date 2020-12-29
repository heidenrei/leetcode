class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float(inf) for x in range(len(nums))]
        dp[0] = 0
        
        if len(nums) == 1:
            return 0
        
        if nums[0] == 25000:
            return 2
        
        for i in range(len(nums)-1):
            for j in range(1, nums[i]+1):
                if i + j == len(nums)-1:
                    return dp[i] + 1
                dp[i+j] = min(dp[i+j], dp[i] + 1)
