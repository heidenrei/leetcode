class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i, x in enumerate(nums):
            if k - x in d:
                return [d[k-x], i]
            d[x] = i