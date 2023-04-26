from sortedcontainers import SortedList

class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        d = defaultdict(list)
        k += 1
        for x, y, z in roads:
            x -= 1
            y -= 1
            d[x].append([y,z])
            d[y].append([x,z])
            
        ans = [x for x in appleCost]
        for i in range(n):
            arrival = defaultdict(lambda: inf)
            arrival[i] = 0
            pq = SortedList([i], key=lambda x: arrival[x])
            while pq:
                curr = pq.pop(0)
                for nei, c in d[curr]:
                    if arrival[nei] > arrival[curr] + c:
                        arrival[nei] = arrival[curr] + c
                        pq.add(nei)
            
            for key, v in arrival.items():
                if key != i and v*k + appleCost[key] < ans[i]:
                    ans[i] = v*k + appleCost[key]
                    
        return ans