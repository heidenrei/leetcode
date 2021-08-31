class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        
        l = 0
        r = N - 1
        
        while l < r:
            m = l + r >> 1
            if nums[l] > nums[r] and nums[m] > nums[r]:
                    l = m + 1
            else:
                r = m
                        
        return nums[l]