class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)
            
        def go(x):
            seen.add(x)
            for nei in d[x]:
                if nei not in seen:
                    go(nei)
        ans = 0
        for x in range(n):
            if x not in seen:
                go(x)
                ans += 1
            
        return ans