class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx = nums.index(max(nums))
        if len(nums) < 2:
            return len(nums) - 1
        return idx if sorted(list(set(nums)))[-1] >= sorted(list(set(nums)))[-2] * 2 else -1