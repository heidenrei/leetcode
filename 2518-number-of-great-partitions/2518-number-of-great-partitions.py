class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        N = len(nums)
        if sum(nums) // 2 < k:
            return 0
        dp = [0]*(k)
        dp[0] = 1
        for i in range(N):
            for j in range(k-1, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] += dp[j-nums[i]]
        
        #print(dp)
                    
        return (pow(2, N, MOD) - (sum(dp)*2))%MOD