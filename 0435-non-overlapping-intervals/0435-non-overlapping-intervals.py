class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prev = -inf
        for x, y in intervals:
            if x < prev:
                prev = min(prev, y)
                ans += 1
            else:
                prev = y
        return ans