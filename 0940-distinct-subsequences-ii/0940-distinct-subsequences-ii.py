class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7
        
        d = defaultdict(int)
        
        for x in s:
            d[x] += 1
            for k in d.keys():
                if k != x:
                    d[x] += d[k]
                    d[x] %= MOD

            
        return sum(d[x] for x in d.keys()) % MOD