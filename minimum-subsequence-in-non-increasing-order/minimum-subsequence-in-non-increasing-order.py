class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        N = len(nums)
        t = sum(nums)
        nums.sort(reverse=True)
        curr_total = nums[0]
        cnt = 1
        
        while curr_total <= t - curr_total:
            curr_total += nums[cnt]
            cnt += 1
            
        return nums[:cnt]
        
