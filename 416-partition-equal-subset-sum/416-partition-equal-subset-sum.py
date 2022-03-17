class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if sum(nums) & 1:
            return False
        @cache
        def go(i, d):
            return d == 0 if i == N else go(i+1, d+nums[i]) or go(i+1, d-nums[i])
        
        return go(0, 0)