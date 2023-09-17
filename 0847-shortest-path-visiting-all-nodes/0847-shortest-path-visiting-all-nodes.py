class Solution:
    def shortestPathLength(self, d: List[List[int]]) -> int:
        cost = defaultdict(lambda: inf)
        N = len(d)
        def bfs(root):
            q = [root]
            seen = set()
            seen.add(root)
            level = 0
            while q:
                tmp = []
                while q:
                    curr = q.pop()
                    for nei in d[curr]:
                        if nei not in seen:
                            key = tuple(sorted([nei, root]))
                            cost[key] = level + 1
                            tmp.append(nei)
                            seen.add(nei)
                level += 1
                q = tmp
                            
        for root in range(N):
            bfs(root)
                
        @cache
        def go(curr, bm):
            if bm == 2**N-1:
                return 0
            ans = inf
            for x in range(N):
                if not bm & (1<<x):
                    key = tuple(sorted([x, curr]))
                    tmp = go(x, bm | (1<<x)) + cost[key]
                    if tmp < ans:
                        ans = tmp
            return ans
        
        best = inf
        for x in range(N):
            tmp = go(x, (1<<x))
            if tmp < best:
                best = tmp
                
        return best