class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        reachable = set()
        bp, ap, bs, als = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        
        def ufind(x, person):
            if person == 2:
                if x not in bp:
                    bp[x] = x
                    bs[x] = 1
                
                if bp[x] != x:
                    bp[x] = ufind(bp[x], 2)
                
                return bp[x]
                
            else:
                if x not in ap:
                    ap[x] = x
                    als[x] = 1
                if ap[x] != x:
                    ap[x] = ufind(ap[x], 1)
                return ap[x]
            
        def uunion(x, y, t):
            if t == 3:
                ux = ufind(x, 1)
                uy = ufind(y, 1)
                if ux != uy:
                    if als[x] > als[y]:
                        uy, ux = ux, uy
                    als[y] += als[x]
                    ap[ux] = uy
                ux = ufind(x, 2)
                uy = ufind(y, 2)
                if ux != uy:
                    if bs[x] > bs[y]:
                        ux, uy = uy, ux
                    bs[uy] += bs[ux]
                    bp[ux] = uy
            elif t == 1:
                ux = ufind(x, 1)
                uy = ufind(y, 1)
                if ux != uy:
                    if als[x] > als[y]:
                        uy, ux = ux, uy
                    als[y] += als[x]
                    ap[ux] = uy
            elif t == 2:
                ux = ufind(x, 2)
                uy = ufind(y, 2)
                if ux != uy:
                    if bs[x] > bs[y]:
                        ux, uy = uy, ux
                    bs[uy] += bs[ux]
                    bp[ux] = uy
        
        need = set()
        
        for t, x, y in sorted(edges, reverse=True):
            if t == 3:
                if ufind(x, 1) != ufind(y, 1) or ufind(x, 2) != ufind(y, 2):
                    uunion(x, y, 3)
                    need.add((t, x, y))
            elif t == 2:
                if ufind(x, 2) != ufind(y, 2):
                    uunion(x, y, 2)
                    need.add((t, x, y))
            elif t == 1:
                if ufind(x, 1) != ufind(y, 1):
                    uunion(x, y, 1)
                    need.add((t, x, y))
        
        p1 = set()
        p2 = set()
        for x in range(1, n+1):
            p1.add(ufind(x, 1))
            p2.add(ufind(x, 2))
            
        if len(p1) > 1 or len(p2) > 1:
            return -1
        
        return len(edges) - len(need)
            