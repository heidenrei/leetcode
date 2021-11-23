class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        d = defaultdict(set)
        p = defaultdict(int)
        s = defaultdict(lambda: 1)
        best = 1
        
        for x in nums:
            s[x]
            p[x] = x
            for factor in range(1, floor(sqrt(x))+1):
                if x/factor % 1 == 0:
                    d[factor].add(x)
                    d[x/factor].add(x)
                    
        def ufind(x):
            if p[x] != x:
                p[x] = ufind(p[x])
            return p[x]
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            
            if s[ux] >= s[uy]:
                uy, ux = ux, uy
                
            s[uy] += s[ux]
            
            nonlocal best
            if s[uy] > best:
                best = s[uy]
            p[ux] = uy
            
        for k, v in d.items():
            if k == 1:
                continue
            d[k] = list(v)
            N = len(d[k])
            for i in range(1, N):
                if ufind(d[k][i]) != ufind(d[k][i-1]):
                    uunion(d[k][i], d[k][i-1])
            
        return best
                        