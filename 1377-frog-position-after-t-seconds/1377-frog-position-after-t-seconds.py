class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, k: int) -> float:
        d = defaultdict(set)
        for x, y in edges:
            d[x].add(y)
            d[y].add(x)
        
        def go(node, rem, prev):
            #print(node, rem, prev)
            if not rem or (len(d[node]) == 1 and node != 1) or len(d[node]) == 0:
                return node == k
            N = len(d[node])
            if node > 1:
                N -= 1
            p = 1/N
            for nei in d[node]:
                if nei != prev:
                    tmp = go(nei, rem-1, node)*p
                    if tmp:
                        return tmp
                
            return 0
        
        return go(1, t, None)