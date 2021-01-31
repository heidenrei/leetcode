class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        
        idx = N - 2
        while idx >= 0 and nums[idx] >= nums[idx+1]:
            idx -= 1
            
        if idx == -1:
            nums.reverse()
            return
        
        idx2 = N-1
        while idx2 >= idx and nums[idx] >= nums[idx2]:
            idx2 -= 1
            
        nums[idx], nums[idx2] = nums[idx2], nums[idx]
        
        l = idx + 1
        r = N - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1