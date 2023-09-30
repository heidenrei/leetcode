from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        sl = SortedList(nums[1:])
        N = len(nums)
        if N < 3:
            return False
        lmin = nums[0]
        for x in nums[1:]:
            sl.remove(x)
            idx = sl.bisect_left(x)
            if idx > 0:
                j = sl[idx-1]
                if j > lmin:
                    return True
            lmin = min(lmin, x)
            
        return False