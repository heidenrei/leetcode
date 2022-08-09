class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        d = defaultdict(list)
        for x, y in connections:
            d[x].append(y)
            d[y].append(x)
            
        connections = set([tuple(x) for x in connections])
        
        seen = set([0])
        
        def dfs(x):
            ans = 0
            for nei in d[x]:
                if nei not in seen:
                    if (x, nei) in connections:
                        ans += 1
                    seen.add(nei)
                    ans += dfs(nei)
            return ans
        
        return dfs(0)