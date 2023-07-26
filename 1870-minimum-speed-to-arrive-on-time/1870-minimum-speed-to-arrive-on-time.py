class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        is_ontime = lambda s: sum(ceil(d / s) for d in dist[:-1]) + dist[-1] / s <= hour
        # low, high = 0, 10**7
        # while low + 1 < high:
        #     mid = low + (high - low) // 2
        #     if is_ontime(mid):
        #         high = mid
        #     else:
        #         low = mid
        # return high if is_ontime(high) else -1
        # def is_good(m):
        #     rem = hour - dist[-1] / m
        #     for x in dist[:-1]:
        #         need = ceil(x/m)
        #         rem -= need
        #         rem = round(rem, 8)
        #         if rem < 0:
        #             return False
            
            
#             return True
        
        l, r = 1, 2**31
        while l <= r:
            m = l + r>> 1
            if is_ontime(m):
                r = m - 1
            else:
                l = m + 1
        return r + 1 if is_ontime(r+1) else -1
            