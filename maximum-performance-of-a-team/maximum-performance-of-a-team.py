from sortedcontainers import SortedList

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9+7
        
        eng = list(zip(efficiency, speed))
        eng.sort(reverse=True)
        
        sl = SortedList(key=lambda x: -x)
        
        best = 0
        speed_multiplier = 0
        for x, y in eng:
            if len(sl) < k:
                speed_multiplier += y
            elif sl.bisect_right(y) < k:
                speed_multiplier -= sl[k-1]
                speed_multiplier += y
            sl.add(y)
            best = max(best, speed_multiplier*x)
            
        return best % MOD