from sortedcontainers import SortedList

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9+7
        
        d = defaultdict(list)
        for x, y, z in edges:
            d[x].append([y,z])
            d[y].append([x,z])
        
        arrival = defaultdict(lambda: inf)
        pq = SortedList(key=lambda x: arrival[x])
        arrival[n] = 0
        pq.add(n)
        
        while pq:
            node = pq.pop(0)
            to_rem = []
            for child, cost in d[node]:
                if arrival[node] + cost < arrival[child]:
                    to_rem.append([node, ])
                    arrival[child] = arrival[node] + cost
                    pq.add(child)
                    
        @cache        
        def dfs(node):
            if node == n:
                return 1
            ans = 0
            for child, cost in d[node]:
                if arrival[node] > arrival[child]:
                    ans += dfs(child)
                    ans %= MOD
                    
            return ans
        
        return dfs(1)