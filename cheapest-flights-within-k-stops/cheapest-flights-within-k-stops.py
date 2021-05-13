class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = [math.inf for x in range(n)]
        
        for parent, child, cost in flights:
            if parent == src:
                dists[child] = cost
                
        dists[src] = 0

                
        for _ in range(k):
            curr = dists[::]
            for parent, child, cost in flights:
                curr[child] = min(curr[child], dists[parent] + cost)
            dists = curr[::]
            
        return dists[dst] if dists[dst] != math.inf else -1