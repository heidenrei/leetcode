class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(set)
        INF = float('inf')
        
        for x, y in edges:
            d[x].add(y)
            d[y].add(x)
        
        best = INF
        
        for x, y in edges:
            for z in d[x] & d[y]:
                score = len(d[x]) + len(d[y]) + len(d[z]) - 6
                if score < best:
                    best = score
            
        return best if best != INF else -1