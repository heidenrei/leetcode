class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        INF = float('inf')
        
        if N < 3:
            return False
        
        min_dp = [0 for x in range(N)]
        max_dp = [0 for x in range(N)]
        mini = INF
        maxi = -INF
        
        for i in range(N):
            mini = min(mini, nums[i])
            min_dp[i] = mini
            
        for i in range(N-1, -1, -1):
            maxi = max(maxi, nums[i])
            max_dp[i] = maxi
            
        for i in range(1, N-1):
            if min_dp[i-1] < nums[i] < max_dp[i+1]:
                return True
            
        return False