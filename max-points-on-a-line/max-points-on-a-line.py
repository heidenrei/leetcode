class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N <= 1:
            return 1
        if N == 2:
            return 2
        points.sort()
        d = defaultdict(set)
        
        # find all the different lines and then count how many points are on each line
        
        for i in range(N):
            for j in range(i):
                if points[i][0] == points[j][0]:
                    slope = 0
                    b = points[i][0]
                elif points[i][1] == points[j][1]:
                    slope = math.inf
                    b = points[i][1]
                else:
                    slope = (points[i][1] - points[j][1])/(points[i][0] - points[j][0])
                    b = -(slope*points[i][0] - points[i][1])
                d[tuple([slope, b])].add(tuple(points[i]))
                d[tuple([slope, b])].add(tuple(points[j]))
        
        best = 1
        
        for k, v in d.items():
            if len(v) > best:
                best = len(v)
                
        return best