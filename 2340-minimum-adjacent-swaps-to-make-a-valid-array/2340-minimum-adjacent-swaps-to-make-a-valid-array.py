class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        mini = min(nums)
        ans = 0
        idx = nums.index(mini)
        ans += idx
        nums = nums[:idx] + nums[idx+1:]
        nums = [-x for x in nums][::-1]
        mini = min(nums)
        idx = nums.index(mini)
        return ans + idx