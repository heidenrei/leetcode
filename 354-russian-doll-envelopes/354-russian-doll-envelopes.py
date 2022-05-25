from sortedcontainers import SortedList

class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: (x[0], -x[1]))
        sl = SortedList()
        for x,y in nums:
            idx = sl.bisect_left(y)
            if idx == len(sl):
                sl.add(y)
            else:
                sl.pop(idx)
                sl.add(y)
        return len(sl)