from sortedcontainers import SortedList

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        dp = [-math.inf for x in range(N)]
        dp[0] = nums[0]
        sl = SortedList([nums[0]])
        
        for i, x in enumerate(nums):
            if i - k - 1 >= 0:
                sl.remove(dp[i-k-1])
            if i != 0:
                dp[i] = sl[-1] + nums[i]
            if i != 0:
                sl.add(dp[i])
                
        return dp[-1]