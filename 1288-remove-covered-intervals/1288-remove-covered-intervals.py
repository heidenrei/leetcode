class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        rem = set()
        eq = set()
        N = len(intervals)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    rem.add(j)
                if intervals[i] == intervals[j]:
                    eq.add(i)
                    eq.add(j)
                    
        return N - len(rem) + len(eq)//2