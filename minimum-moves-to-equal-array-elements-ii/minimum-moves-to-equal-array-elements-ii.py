class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        if N == 2:
            return abs(nums[0] - nums[1])
        
        nums.sort()
        if N & 1:
            ans = 0
            for num in nums:
                ans += abs(num - nums[N//2])
            return ans
        
        ans_left = 0
        ans_right = 0
        for num in nums:
            ans_left += abs(num - nums[N//2])
            ans_right += abs(num - nums[N//2+1])
            
        return min(ans_left, ans_right)