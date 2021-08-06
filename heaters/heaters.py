from sortedcontainers import SortedList

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses:
            return 0
        
        houses = list(set(houses))
        heaters = list(set(heaters))
        
        N = len(houses)
        
        sl = SortedList(heaters)
        
        best = 0
        
        for x in houses:
            idx = sl.bisect_left(x)
            tmp = math.inf
            if idx >= 1:
                tmp = abs(x - sl[idx-1])
            if idx + 1 < len(heaters):
                tmp = min(tmp, abs(x - sl[idx+1]))
            if 0 <= idx < len(heaters):
                tmp = min(tmp, abs(x - sl[idx]))
            
            best = max(best, tmp)
            
        return best
        
            
        