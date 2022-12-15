class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        mh = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        N, M = len(workers), len(bikes)
        
        @cache
        def go(i, bm):
            if i == N:
                return 0
            ans = inf
            for j in range(M):
                if not bm & (1<<j):
                    tmp = go(i+1, bm | (1<<j)) + mh(workers[i], bikes[j])
                    if tmp < ans:
                        ans = tmp
                        
            return ans
        
        return go(0, 0)
        
            
            
                