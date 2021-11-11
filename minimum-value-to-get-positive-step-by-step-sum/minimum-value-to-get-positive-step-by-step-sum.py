import copy
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        N = len(nums)
        best = math.inf
        def is_good(curr):
            for i in range(N):
                curr += nums[i]
                if curr < 1:
                    return False
            return True
                
        l = 1
        r = 100*101
        while l < r:
            m = (l+r) >> 1
            
            if is_good(m):
                r = m
            else:
                l = m + 1
                
        return l