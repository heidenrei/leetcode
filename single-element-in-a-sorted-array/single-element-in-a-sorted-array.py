class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = N - 1
        
        while l < r:
            m = l + r >> 1
            if m & 1:
                if nums[m] == nums[m-1]:
                    l = m + 1
                else:
                    r = m
            else:
                if nums[m] == nums[m+1]:
                    l = m + 1
                else:
                    r = m
                    
        return nums[l]