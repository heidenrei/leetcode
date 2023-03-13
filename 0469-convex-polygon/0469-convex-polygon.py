class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def orientation(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p3
            x3, y3 = p2
            return (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)
        points += points
        N = len(points)
        good = True
        for i in range(N-2):
            p1, p2, p3 = points[i], points[i+1], points[i+2]
            if orientation(p1,p2,p3) > 0:
                good = False
                break
        if good:
            return True
        points.reverse()
        good = True
        for i in range(N-2):
            p1, p2, p3 = points[i], points[i+1], points[i+2]
            if orientation(p1,p2,p3) > 0:
                good = False
                break
        if good:
            return True
        return False
        