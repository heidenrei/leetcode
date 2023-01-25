class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # bfs from each
        N = len(edges)
        d1 = [inf for x in range(N)]
        d2 = [inf for x in range(N)]
        
        q = [node1]
        seen = set([node1])
        level = 0
        while q:
            tmp = []
            while q:
                node = q.pop()
                d1[node] = level
                if edges[node] >= 0 and edges[node] not in seen:
                    seen.add(edges[node])
                    tmp.append(edges[node])
            q = tmp
            level += 1
        
        seen = set([node2])
        q = [node2]
        level = 0
        while q:
            tmp = []
            while q:
                node = q.pop()
                d2[node] = level
                if edges[node] >= 0 and edges[node] not in seen:
                    seen.add(edges[node])
                    tmp.append(edges[node])
            q = tmp
            level += 1
        
#         print(d1)
#         print(d2)
        
        best = inf
        besti = None
        for i in range(N):
            if max(d1[i], d2[i]) < best:
                best = max(d1[i], d2[i])
                besti = i
                
        return besti if besti is not None else -1