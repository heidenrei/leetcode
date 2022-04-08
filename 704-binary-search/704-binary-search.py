class Solution:
    def search(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = l + r >> 1
            if nums[m] == k:
                return m
            if nums[m] < k:
                l = m + 1
            else:
                r = m
                
        return -1