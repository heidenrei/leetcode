class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        jumps = [1,7,30]
        @cache
        def go(i):
            if i == len(days):
                return 0
            ans = inf
            for j in range(3):
                idx = bisect_left(days, days[i] + jumps[j])
                tmp = go(idx) + costs[j]
                if tmp < ans:
                    ans = tmp
            return ans
        
        return go(0)