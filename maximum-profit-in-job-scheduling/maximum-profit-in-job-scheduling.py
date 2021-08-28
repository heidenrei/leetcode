class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)

        times = []
        for i in range(N):
            times.append([startTime[i], endTime[i], profit[i]])
            
        times.sort()
        
        for idx, [x, y, z] in enumerate(times):
            startTime[idx] = x
            endTime[idx] = y
            profit[idx] = z
        
        @cache
        def go(i):
            if i == N:
                return 0
            best = 0
            
            next_idx = bisect.bisect_left(startTime, endTime[i])
            best = max(best, go(next_idx) + profit[i])
            best = max(best, go(i+1))
                
            return best
        
        return go(0)