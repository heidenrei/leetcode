class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7
        
        d = defaultdict(int)
        
        for x in s:
            tmp = 0
            for k in d.keys():
                if k != x:
                    tmp += d[k]
                    tmp %= MOD

            d[x] += tmp + 1
            d[x] %= MOD

            
        return sum(d[x] for x in d.keys()) % MOD