class Solution(object):
    def maximumGap(self, nums):
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)[::-1]
        diffs = []
        for i in range(len(nums)-1):
            diffs.append(nums[i]-nums[i+1])
        return max(diffs)
