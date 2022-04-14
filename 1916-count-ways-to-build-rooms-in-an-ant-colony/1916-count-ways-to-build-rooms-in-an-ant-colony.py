class Solution:
    def waysToBuildRooms(self, rooms):
        # at each node return product of num ways of children * nCr of children node count
        MOD = 10**9+7
        @cache
        def f(x):
            if x <= 1:
                return 1
            ans = f(x-1) * x
            return ans % MOD

        def mi(x, y):
            #y **= (MOD-2)
            y = pow(y, MOD-2, MOD)
            #y %= MOD
            ans = x * y
            ans %= MOD
            return ans
        
        d = defaultdict(list)
        N = len(rooms)
        #print(N)
        for i in range(N):
            d[rooms[i]].append(i)
        
        def go(node): # -> ways, node_cnt
            if node not in d:
                return 1, 1
            ways = 1
            cnts = []
            
            for child in d[node]:
                cways, ccnt = go(child)
                ways *= cways
                ways %= MOD
                cnts.append(ccnt)
                
            p = 1
            scnts = 0
            for c in cnts:
                p *= f(c)
                scnts += c
            
            #ways *= f(scnts) // p
            ways *= mi(f(scnts), p)
            ways %= MOD
            return ways, sum(cnts) + 1
        return go(0)[0]
                
            
        
