class Solution:
    def search(self, nums: List[int], k: int) -> int:
        l, r= 0, len(nums)-1
        while l < r:
            m = l + r >> 1
            if nums[m] < k:
                l = m + 1
            else:
                r = m
        
        if nums[l] == k:
            return l
        if nums[l-1] == k:
            return l - 1
        
        return -1