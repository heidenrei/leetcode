class Solution:
    def maxValue(self, A, k: int) -> int:
        #need list of events starting after day x...sort events by x[0] then events[bisectright:] to find valid events
        #memo k + day
        N = len(A)
        A.sort()
        
        @lru_cache(None)
        def go(i, rem):
            if i >= N or rem == 0:
                return 0
            
            # A[j] is the next event you can attend
            j = bisect_right(A, [A[i][1], math.inf])
            take = A[i][2] + go(j, rem-1)
            dont_take = go(i+1, rem)
            return max(take, dont_take)
        
        
        return go(0, k)