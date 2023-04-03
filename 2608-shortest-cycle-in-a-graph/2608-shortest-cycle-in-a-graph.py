class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)
        ans = inf
        def go(x, n):
            nonlocal ans
            q = [x]

            arrival = [0 for x in range(n)]
            arrival[x] = 1
            p = [0 for x in range(n)]
            level = 0
            while q:
                tmp = set()
                tmp_arrival = set()
                qset = set(q)
                for curr in q:
                    for nei in d[curr]:
                        if not arrival[nei]:
                            if nei in tmp:
                                if (level+1)*2 < ans:
                                    ans = (level+1)*2
                                    
                            tmp.add(nei)

                            tmp_arrival.add(nei)
                            p[nei] = curr
                        elif p[curr] != nei and nei in qset:
                            if level*2+1 < ans:
                                ans = level*2+1
                        
                
                level += 1

                for y in tmp_arrival:
                    arrival[y] = 1
                q = tmp
                
        
        for x in range(n):
            go(x, n)
            
        return ans if ans < inf else -1