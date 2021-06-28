from sortedcontainers import SortedList

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        
        ans = []
        sl = SortedList()
        
        for idx, x in enumerate(intervals):
            sl.add([x[0], x[1], idx])
                
        for x, y in intervals:
            idx = sl.bisect([y, -math.inf, -math.inf])
            if idx == N:
                ans.append(-1)
            else:
                ans.append(sl[idx][2])
    
        return ans