from sortedcontainers import SortedList

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        sl = SortedList()
        for x in obstacles:
            idx = sl.bisect_right(x)
            if idx < len(sl):
                sl.pop(idx)
            ans.append(idx+1)
            sl.add(x)
            
        return ans