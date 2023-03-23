class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
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
            if s[ux] > s[uy]:
                ux, uy = uy, ux
            s[uy] += s[ux]
            p[ux] = uy
        
        extra = 0
        for x, y in connections:
            if ufind(x) != ufind(y):
                uunion(x, y)
            else:
                extra += 1
        ans = 0
        for x in range(n):
            if ufind(x) != ufind(0):
                if extra:
                    extra -= 1
                    ans += 1
                    uunion(x, 0)
        
        if s[ufind(0)] < n:
            return -1
        
        return ans