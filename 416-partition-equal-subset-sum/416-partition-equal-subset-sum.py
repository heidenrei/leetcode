class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        k = sum(nums)/2
        if k % 1 != 0:
            return False
        @cache
        def go(i, d):
            if i == N:
                return d == 0
            return go(i+1, d+nums[i]) or go(i+1, d-nums[i])
        
        return go(0, 0)