from sortedcontainers import SortedList

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        arrival_time = defaultdict(lambda: inf)
        arrival_time[0] = 0
        pq = SortedList(key = lambda x: arrival_time[x])
        pq.add(0)
        d = defaultdict(list)
        
        for x, y, z in edges:
            d[x].append([y, z])
            d[y].append([x, z])
        
        while pq:
            curr = pq.pop(0)
            for x, cost in d[curr]:
                if arrival_time[curr] + cost + 1 < arrival_time[x]:# and arrival_time[curr] + cost + 1 <= maxMoves:
                        arrival_time[x] = arrival_time[curr] + cost + 1
                        pq.add(x)
                    
                    
        ans = 0
        #print(arrival_time)
        already_answered = set()
        for k, v in arrival_time.items():
            if v < maxMoves:
                for x, cost in d[k]:
                    if tuple(sorted([k, x])) not in already_answered:
                        
                        if arrival_time[x] <= maxMoves:
                            ans += min(cost, min(maxMoves - arrival_time[k], cost) + min(maxMoves - arrival_time[x], cost))
                        else:
                            ans += maxMoves - arrival_time[k]
                            print(k, x)
                        #print(k, x, min(cost, min(maxMoves - arrival_time[k], cost) + min(maxMoves - arrival_time[x], cost)))
                        already_answered.add(tuple(sorted([k, x])))
        
        for v in arrival_time.values():
            if v <= maxMoves:
                ans += 1
                    
        return ans