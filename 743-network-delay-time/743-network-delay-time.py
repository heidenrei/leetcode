from sortedcontainers import SortedList

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for x,y,z in times:
            d[x].append([y,z])
        sl = SortedList(key=lambda x: arrival[x])
        arrival = defaultdict(lambda: inf)
        seen = set()
        seen.add(k)
        arrival[k] = 0
        sl.add(k)
        while sl:
            x = sl.pop(0)
            for child, dt in d[x]:
                if arrival[child] > arrival[x] + dt:
                    arrival[child] = arrival[x] + dt
                    sl.add(child)
                    seen.add(child)
        
        
        return max(arrival.values()) if len(seen) == n else -1
        