class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        N = len(points)
        best = 0
        
        def ed(p1, p2):
            return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        for i in range(N):
            for j in range(i):
                for k in range(j):
                    if i != j != k:
                        b = ed(points[i], points[j])
                        x1, y1 = points[i]
                        x2, y2 = points[j]
                        x0, y0 = points[k]
                        h = abs((x2-x1)*(y1-y0) - (x1-x0)*(y2-y1))/sqrt((x2-x1)**2+(y2-y1)**2)
                        tmp = (h*b)/2
                        if tmp > best:
                            best = tmp
        return best