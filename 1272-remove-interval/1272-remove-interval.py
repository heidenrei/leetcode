class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        N = len(intervals)
        l, r = toBeRemoved
        
        for i in range(N):
            if intervals[i][0] <= l and intervals[i][1] >= r:
                new_left = [intervals[i][0], l]
                new_right = [r, intervals[i][1]]
                intervals.remove(intervals[i])
                if new_left[0] != new_left[1]:
                    intervals.append(new_left)
                if new_right[0] != new_right[1]:
                    intervals.append(new_right)
                    
                intervals.sort()
                return intervals
        lidx = bisect_right(intervals, [l, inf])
        ridx = bisect_left(intervals, [r, -inf])
        if lidx > 0:
            intervals[lidx-1][1] = min(l, intervals[lidx-1][1])
        #print(intervals)
        if ridx > 0 and intervals[ridx-1][1] > r:
            intervals[ridx-1][0] = max(r, intervals[ridx-1][0])
        #print(intervals)
        return [x for x in intervals if not l < x[0] < r]