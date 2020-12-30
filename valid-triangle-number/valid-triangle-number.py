import bisect
​
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # N**2*log(N)
        # N = 10*3
        # upper bound ~= 10**8
        
        N = len(nums)
        
        if N < 3:
            return 0
        
        nums.sort()
        cnt = 0
        
        for r in range(2, N):
            for m in range(1, r):
                idx = bisect.bisect_left(nums, nums[r] - nums[m] + 1)
                cnt += m - idx if idx < m else 0
                
        return cnt
