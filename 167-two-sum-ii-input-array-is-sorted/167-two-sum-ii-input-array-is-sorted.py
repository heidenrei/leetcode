class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        for i in range(N):
            idx = bisect.bisect_left(nums, k-nums[i])
            if idx < len(nums) and idx != i:
                if nums[idx] + nums[i] == k:
                    return sorted([idx+1, i+1])