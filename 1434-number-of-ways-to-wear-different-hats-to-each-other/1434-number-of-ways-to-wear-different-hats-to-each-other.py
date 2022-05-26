class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9+7
        N = len(hats)
        d = defaultdict(list)
        for i in range(N):
            for j in range(len(hats[i])):
                d[hats[i][j]].append(i)
    
        @cache
        def go(i, bm):
            if bm == 2**N-1:
                return 1
            if i == 41:
                return 0
            ans = go(i+1, bm)
            for j in d[i]:
                if not bm & (1<<j):
                    ans += go(i+1, bm | (1<<j))
                    ans %= MOD
                    
            return ans
        
        return go(1, 0)
        