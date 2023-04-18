class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7
        N = len(s)
        d = defaultdict(int)
        
        for x in s:
            d[x] += 1# + N - d[x]
            #d[x] += N
            #d[x] -= d[x]
            for k in d.keys():
                if k != x:
                    d[x] += d[k]
                    d[x] %= MOD

            
        return sum(v for v in d.values()) % MOD