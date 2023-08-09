class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N = len(nums)
        def is_good(m):
            tums = deque(nums)
            tp = p
            while tp and len(tums) >= 4:
                if tums[1] - tums[0] <= m:
                    tums.popleft();tums.popleft()
                    tp -= 1
                else:
                    tums.popleft()
                if tums[-1] - tums[-2] <= m:
                    tums.pop();tums.pop()
                    tp -= 1
                else:
                    tums.pop()
                    

            if len(tums) == 3:
                if tums[1] - tums[0] <= m or tums[-1] - tums[-2] <= m:
                    tp -= 1
            elif len(tums) == 2:
                if tums[-1] - tums[-2] <= m:
                    tp -= 1
            
            return tp <= 0
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            m = l + r >> 1
            if is_good(m):
                r = m - 1
            else:
                l = m + 1
        return r+1