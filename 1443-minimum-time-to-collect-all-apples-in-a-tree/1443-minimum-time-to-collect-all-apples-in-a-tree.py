class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d = defaultdict(int)
        d2 = defaultdict(set)
        for x, y in edges:
            d2[y].add(x)
            d2[x].add(y)
            
        def go(node):
            for child in d2[node]:
                d2[child].remove(node)
                go(child)
                
        go(0)
        for k, v in d2.items():
            v = list(v)
            if v:
                for x in v:
                    d[x] = k
        
        
        #print(d)
        
        seen = set()
        ans = 0
        def go(node):
            nonlocal ans
            seen.add(node)
            if node in d and not hasApple[node]:# and not hasApple[d[node]]:
                ans += 2
            if node in d and d[node] not in seen and not hasApple[d[node]]:
                go(d[node])
        
        for i, x in enumerate(hasApple):
            if x:
                go(i)
        
        return ans + sum(hasApple)*2 - hasApple[0]*2
                