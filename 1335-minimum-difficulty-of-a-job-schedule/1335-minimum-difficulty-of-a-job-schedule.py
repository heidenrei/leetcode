class Solution:
    def minDifficulty(self, jobs, d):
        N = len(jobs)
        @cache
        def go(i, rem):
            if i == N:
                if not rem:
                    return 0
                else:
                    return inf
            best = inf
            m = 0
            for ni in range(i, N):
                #m = max(m, jobs[ni])
                if jobs[ni] > m:
                    m = jobs[ni]
                tmp = go(ni+1, rem-1) + m
                if best > tmp:
                    best = tmp
            return best
        
        return go(0, d) if go(0, d) < inf else -1