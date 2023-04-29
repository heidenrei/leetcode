class Solution:
    def distanceLimitedPathsExist(self, n: int, edges, queries):
        p = defaultdict(int)
        s = defaultdict(lambda: x)
        
        def ufind(x):
            if x not in p:
                p[x] = x
                s[x]
            if p[x] != x:
                p[x] = ufind(p[x])
            return p[x]
        
        def uunion(x, y):
            ux, uy = ufind(x), ufind(y)
            if ux == uy:
                return
            if s[ux] > s[uy]:
                ux, uy = uy, ux
            s[uy] += s[ux]
            p[ux] = uy
        
        q = len(queries)
        for i in range(q):
            queries[i].append(i)
        ans = [False]*q
        queries.sort(key=lambda x: -x[2])
        edges.sort(key=lambda x: -x[2])
        while queries:
            if edges and edges[-1][2] < queries[-1][2]:
                x, y, _ = edges.pop()
                uunion(x, y)
            else:
                x, y, _, i = queries.pop()
                ans[i] = ufind(x) == ufind(y)
        return ans
                    