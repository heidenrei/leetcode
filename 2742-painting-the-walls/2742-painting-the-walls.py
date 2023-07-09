class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(cost)    
        @cache
        def go(i, t):
            if N-i <= t:
                return 0
            if i == N:
                if t >= 0:
                    return 0
                else:
                    return inf
            return min(go(i+1, t + time[i]) + cost[i], go(i+1, t-1))
        return go(0, 0)
    
            