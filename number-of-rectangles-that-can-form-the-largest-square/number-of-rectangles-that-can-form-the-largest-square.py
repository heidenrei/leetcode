class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        best = 0
        cnt = 0
        for i in range(len(rectangles)):
            mini = min(rectangles[i])
            if mini == best:
                cnt += 1
                best = mini
            elif mini > best:
                cnt = 1
                best = mini
            
        return cnt
