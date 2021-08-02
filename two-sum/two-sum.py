class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for idx, x in enumerate(nums):
            if target - x in seen:
                return [seen[target-x], idx]
            seen[x] = idx