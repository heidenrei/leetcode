class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        curr = -math.inf
        for s, e in intervals:
            if s < curr:
                ans += 1
                curr = min(curr, e)
            else:
                curr = e
                
        return ans