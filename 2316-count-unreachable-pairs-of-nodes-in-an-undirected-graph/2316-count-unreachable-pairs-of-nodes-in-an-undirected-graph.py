class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:            
        p = defaultdict(int)
        s = defaultdict(lambda: 1)
        
        def ufind(x):
            if x not in p:
                p[x] = x
                s[x]
            if p[x] != x:
                p[x] = ufind(p[x])
            return p[x]
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            if ux == uy:
                return
            # if s[ux] > s[uy]:
            #     ux, uy = uy, ux
            s[uy] += s[ux]
            p[ux] = uy
            
        seen = set()
        for x, y in edges:
            uunion(x, y)
        ans = 0

        for x in range(n):
            ux = ufind(x)
            if ux not in seen:
                seen.add(ux)
                ans += s[ux] * (n-s[ux])
        
        return ans//2
            