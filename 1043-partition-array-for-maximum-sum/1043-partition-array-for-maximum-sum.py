class Solution:
    def maxSumAfterPartitioning(self, nums, k):
        N = len(nums)
        @cache
        def go(i, j, val):
            if j == N:
                return val*(j-i)
            
            pick = go(j, j+1, nums[j]) + val*(j-i)
            if j - i < k:
                pss = go(i, j+1, max(val, nums[j]))
            else:
                pss = pick
            return max(pick, pss)
        return go(0, 1, nums[0])
                