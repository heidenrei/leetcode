class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 1
        for n in range(1, max(nums)+2):
            if n not in nums:
                return n
        return 1
