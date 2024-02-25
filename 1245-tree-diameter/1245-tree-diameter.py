class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        ind = defaultdict(int)
        for x, y in edges:
            d[x].append(y);d[y].append(x)
            ind[x] += 1;ind[y] += 1
        root = None
        for k, v in ind.items():
            if v == 1:
                root = k
        best = 0
        @cache
        def go(x, prev):
            nonlocal best
            ans = 0
            children = [0,0]
            for child in d[x]:
                if child != prev:
                    children.append(go(child, x))
            children.sort()
            best = max(best, 1 + children[-1] + children[-2])
            return children[-1] + 1
        go(root, None)
        return best - 1
        