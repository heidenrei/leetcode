class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        best = 0
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            if nums[i-2] < (nums[i-1] + nums[i]):
                best = max(best, sum(nums[i-2:i+1]))
                
        return best