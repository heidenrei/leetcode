
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target):        
        N = len(routes)
        
        routes = [set(x) for x in routes]
        
        d = defaultdict(list)
        seen = set()
        
        for i in range(N):
            for r in routes[i]:
                d[r].append(i)
        
        
        q = deque([source])
        
        level = 0
        while q:
            tmp = []
            while q:
                curr = q.popleft()
                if curr == target:
                    return level
                for idx in d[curr]:
                    if idx not in seen:
                        seen.add(idx)
                        for dest in routes[idx]:
                            tmp.append(dest)
                        
            q.extend(tmp)
            level += 1
        return -1
            
        
        
        