class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for x, y in paths:
            d[x].append(y)
            d[y].append(x)
        ans = [None for x in range(n)]
        def go(x, prev):
            available = set([1, 2, 3, 4])
            for nei in d[x]:
                if ans[nei-1] in available:
                    available.remove(ans[nei-1])
            available = list(available)
            ans[x-1] = available[0]
            for nei in d[x]:
                if nei != prev and ans[nei-1] is None:
                    go(nei, x)
        
        for x in range(1, n+1):
            if ans[x-1] is None:
                go(x, None)
        return ans
            