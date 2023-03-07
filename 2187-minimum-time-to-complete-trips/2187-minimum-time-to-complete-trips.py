class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def is_good(k):
            trips = 0
            for x in time:
                trips += k // x
            return trips >= totalTrips
        
        l = 0
        r = max(time) * totalTrips
        while l <= r :
            m = l + r >> 1
            if is_good(m):
                r = m - 1
            else:
                l = m + 1
                
        return r + 1