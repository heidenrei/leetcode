class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(set)
        INF = float("inf")
        distances = [INF]*n
        seen = frozenset()
        odd = False
        get_mid = False
        ans = []
        for i, j in edges:
            d[i].add(j)
            d[j].add(i)
        
        def go(node, p, curr_distance):
            distances[node] = curr_distance
            
            for dest in d[node]:
                if dest != p:
                    go(dest, node, curr_distance + 1)
                    
        go(0, None, 1)
        print(distances)
        farthest_node = max(distances)
        rerun_node = distances.index(max(distances))
        
        distances = [INF]*n
        
        go(rerun_node, None, 1)
        
        print(distances)
        
        maxi = max(distances)
        
        if maxi & 1:
            return [distances.index(maxi//2+1)]
        else:
            return [distances.index(maxi//2+1), distances.index(maxi//2)]