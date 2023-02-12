from sortedcontainers import SortedList

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        rd = defaultdict(list)
        bd = defaultdict(list)
        for x, y in redEdges:
            rd[x].append(y)
        for x, y in blueEdges:
            bd[x].append(y)
        
        def dj(x, color):
            pq = SortedList(key=lambda x: arrival[x])
            arrival = defaultdict(lambda: inf)
            arrival[(0, color)] = 0
            pq.add((0, color))
            while pq:
                tmp = []
                while pq:
                    curr, color = pq.pop(0)
                    #print(curr, color)
                    if curr == x:
                        #print('1111111', x)
                        return arrival[(curr, color)]
                    if color == 1:
                        for nei in rd[curr]:
                            if arrival[(nei, 1^color)] > arrival[(curr, color)] + 1:
                                arrival[(nei, 1^color)] = arrival[(curr, color)] + 1
                                pq.add((nei, color ^ 1))
                    if color == 0:
                        for nei in bd[curr]:
                            if arrival[(nei, 1^color)] > arrival[(curr, color)] + 1:
                                arrival[(nei, 1^color)] = arrival[(curr, color)] + 1
                                pq.add((nei, color^1))
            return inf
                                
        ans = []
        
        #print(dj(1, 'b'))
        
        
        for x in range(n):
            ans.append(min(dj(x, 1), dj(x, 0)))
            if ans[-1] == inf:
                ans[-1] = -1
        return ans