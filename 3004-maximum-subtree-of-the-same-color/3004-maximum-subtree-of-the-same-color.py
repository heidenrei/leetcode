class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)
        ret = 0
        def go(node, parent):
            ans = 1
            for child in d[node]:
                if child == parent:
                    continue
                if colors[child] != colors[node]:
                    ans = -inf
                    go(child, node)
                else:
                    ans += go(child, node)
                
            nonlocal ret
            ret = max(ans, ret)
            return ans
        go(0, None)
        return ret