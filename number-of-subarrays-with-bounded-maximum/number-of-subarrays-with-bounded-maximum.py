class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], low: int, high: int) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] > high:
                nums[i] = "!"
        
        curr = 0
        ans = 0
        for i in range(N):
            if nums[i] == '!':
                curr = 0
            else:
                curr += 1
            ans += curr
        
        curr = 0
        
        for i in range(N):
            if nums[i] != '!' and nums[i] < low:
                curr += 1
            else:
                curr = 0
            ans -= curr
        
        return ans