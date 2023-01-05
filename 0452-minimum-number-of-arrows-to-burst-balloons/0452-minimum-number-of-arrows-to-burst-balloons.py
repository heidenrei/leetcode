class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N = len(points)
        ans = 0
        popped = set()
        points = [[i] + points[i] for i in range(N)]
        times = []
        opn = set()
        closes = defaultdict(list)
        opens = defaultdict(list)
        for i, x, y in points:
            opens[x].append(i)
            closes[y].append(i)
            times.append(x)
            times.append(y)
            
        times.sort()
        for time in times:
            if time in opens:
                for x in opens[time]:
                    opn.add(x)
            if time in closes:
                for x in closes[time]:
                    if x not in popped:
                        ans += 1
                        popped |= opn
                        opn = set()
                        
        return ans
        