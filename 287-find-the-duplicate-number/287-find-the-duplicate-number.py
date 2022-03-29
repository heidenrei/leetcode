class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bm = 0
        for x in nums:
            if bm & (1<<x):
                return x
            bm |= (1<<x)