class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        N = len(nums)
        if sum(nums) < k:
            return 0
        
        def is_good(x):
            curr = sum(nums[:x])
            if curr >= k:
                return True
            for i in range(x, N):
                curr += nums[i] - nums[i-x]
                if curr >= k:
                    return True
            return False
        
        l, r = 1, N
        while l <= r:
            m = l + (r-l+1)//2
            if is_good(m):
                r = m - 1
            else:
                l = m + 1
        return r+1
        
        