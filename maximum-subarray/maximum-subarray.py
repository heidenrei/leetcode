class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        N = len(nums)
        
        nums = [float('-inf')] + nums
        
        for i in range(1, N+1):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
            
        return max(nums)