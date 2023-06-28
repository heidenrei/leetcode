from sortedcontainers import SortedList

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        N = len(edges)
        d = defaultdict(list)
        for i in range(N):
            d[edges[i][0]].append([edges[i][1], succProb[i]])
            d[edges[i][1]].append([edges[i][0], succProb[i]])
        pq = SortedList(key=lambda x: -arrival[x])
        arrival = defaultdict(int)
        arrival[start] = 1
        pq.add(start)
        while pq:
            curr = pq.pop(0)
            if curr == end:
                return arrival[end]
            for nei, p in d[curr]:
                if arrival[nei] < arrival[curr] * p:
                    arrival[nei] = arrival[curr] * p
                    pq.add(nei)
        return 0