from sortedcontainers import SortedList

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1]*len(queries)
        
        events = []
        
        for idx, (s, e) in enumerate(intervals):
            events.append([s, e, 0, idx])
            events.append([e, math.inf, 2, idx])

        for idx, val in enumerate(queries):
            events.append([val, 10**8, 1, idx])
            
            
        events.sort()
        
        print(events)
        
        sl = SortedList()
        for s, e, t, i in events:
            if t == 0:
                sl.add([intervals[i][1] - intervals[i][0] + 1, i])
            elif t == 1:
                if sl:
                    ans[i] = sl[0][0]
            else:
                sl.remove([intervals[i][1] - intervals[i][0] + 1, i])
                
        return ans