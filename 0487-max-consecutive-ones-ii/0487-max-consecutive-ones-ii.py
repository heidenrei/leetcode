class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pfs = list(accumulate(nums, initial=0))
        N = len(pfs)
        
        def is_good(x):
            for i in range(x, N):
                if pfs[i] - pfs[i-x] >= x-1:
                    return True
            return False
        
        l, r = 1, N
        while l < r:
            m = l + (r-l+1)//2
            if is_good(m):
                l = m
            else:
                r = m - 1
        return l