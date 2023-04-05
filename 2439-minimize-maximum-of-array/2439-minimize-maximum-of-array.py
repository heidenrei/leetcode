class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        N = len(nums)
        def is_good(x):
            tums = [y for y in nums]
            for i in range(N-1, 0, -1):
                if tums[i] > x:
                    tums[i-1] += tums[i] - x
            return tums[0] <= x
        
        
        
        l, r = min(nums), max(nums)
        
        # for x in range(l, r+1):
        #     print(x, is_good(x))
        while l < r:
            m = l + r >> 1
            if is_good(m):
                r = m - 1
            else:
                l = m + 1
        if is_good(r):
            return r
        return r+1