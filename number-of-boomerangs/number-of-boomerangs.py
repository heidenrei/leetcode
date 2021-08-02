class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        N = len(points)
        
        def e(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            return ((x1-x2)**2 + (y1 - y2)**2)
            
        d = defaultdict(int)
        
        for i in range(N):
            for j in range(N):
                if i != j:
                    d[tuple([i, e(i, j)])] += 1
                    
        ans = 0
                
        for v in d.values():
            if v >= 2:
                ans += (v*(v-1))
            
        return ans