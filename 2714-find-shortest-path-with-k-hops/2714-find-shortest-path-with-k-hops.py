from sortedcontainers import SortedList

class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, dest: int, k: int) -> int:
        d = defaultdict(list)
        for x, y, w in edges:
            d[x].append([y, w])
            d[y].append([x, w])
        arrival = defaultdict(lambda: inf)
        arrival[(s, 0)] = 0
        pq = SortedList(key=lambda x: arrival[x])
        pq.add((s, 0))
        while pq:
            currn, currk = pq.pop(0)
            #print(currn)
            if currn == dest:
                return arrival[(currn, currk)]
            for nei, w in d[currn]:
                #print(nei, w)
                if arrival[(currn, currk)] + w < arrival[(nei, currk)]:
                    arrival[(nei, currk)] = arrival[(currn, currk)] + w
                    pq.add((nei, currk))
                if currk + 1 <= k and arrival[(currn, currk)] < arrival[(nei, currk+1)]:
                    arrival[(nei, currk+1)] = arrival[(currn, currk)]
                    pq.add((nei, currk+1))
        return -1
            