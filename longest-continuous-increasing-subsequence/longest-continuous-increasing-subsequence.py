class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        best = 1
        curr = 1
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                curr += 1
                best = max(best, curr)
            else:
                curr = 1
                
        return best