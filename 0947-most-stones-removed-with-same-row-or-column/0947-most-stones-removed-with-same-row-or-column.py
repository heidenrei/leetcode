class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        p = defaultdict(int)
        s = defaultdict(int)
        
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
            if s[ux] > s[uy]:
                ux, uy = uy, ux
            s[uy] += s[ux]
            p[ux] = uy
        
        for i, (x0, y0) in enumerate(stones):
            for x1, y1 in stones[i+1:]:
                if x0 == x1 or y0 == y1:
                    uunion(tuple([x0, y0]), tuple([x1, y1]))
        
        dsus = set()
        for x in stones:
            dsus.add(ufind(tuple(x)))
        return len(stones) - len(dsus)