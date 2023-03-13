class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = list(set([tuple(x) for x in points]))
        d = defaultdict(list)
        for x,y in points:
            d[y].append(x)
        m = None
        #print(d)
        for v in d.values():
            v.sort()
            N = len(v)
            if N & 1:
                tm = v[N//2]
            else:
                tm = (v[N//2] + v[N//2-1])/2
            if m is None:
                m = tm 
            for i in range(N//2+(N&1)):
                l = v[i]
                r = v[N-i-1]
                tm = (l+r)/2
                #print(l, r, m)
                if tm != m:
                    return False
        return True
            
        