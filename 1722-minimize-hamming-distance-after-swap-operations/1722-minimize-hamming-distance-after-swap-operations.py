class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)
        parent = defaultdict(int)
        size = defaultdict(lambda: 1)

        def ufind(x):
            if x not in parent:
                parent[x] = x
                size[x]
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            if size[ux] > size[uy]:
                uy, ux = ux, uy
            
            size[uy] += size[ux]
            parent[ux] = uy
            
        
        for x, y in allowedSwaps:
            uunion(x, y)
        
        m = defaultdict(set)
        for i in range(N):
            #if i in parent:
            m[ufind(i)].add(i)
        
        cnt = N
        
        for v in m.values():
            A = Counter([source[i] for i in v])
            B = Counter([target[i] for i in v])
            for k, val in B.items():
                cnt -= min(val,A[k]) 
            
        
                
        return cnt
                
                
        