class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parents = [x for x in range(n+1)]
        out = []
        
        if threshold == 0:
            return [True]*len(queries)
        
        def ufind(x):
            if parents[x] != x:
                x = ufind(parents[x])
            return x
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            parents[ux] = uy
        
        @lru_cache(None)
        def get_gcd(i, j):
            if math.gcd(i+1, j+1) > threshold:
                return True
        
        for x in range(threshold + 1, n+1):
            k = x
            while k < n+1:
                uunion(x, k)
                k += x
                    
        for x, y in queries:
            if ufind(x) == ufind(y):
                out.append(True)
            else:
                out.append(False)
                
        return out
