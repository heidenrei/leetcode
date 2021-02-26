class Solution:
    def isRectangleCover(self, A):
        # xor out internal corners (cause they'll appear twice)
        # sum up area of all the rectangles and make sure that it matches the area of the remaining corners
        
        total_area = 0
        corners = set()
        
        for x1, y1, x2, y2 in A:
            total_area += (x2-x1)*(y2-y1)
            corners ^= {tuple([x1, y1])}
            corners ^= {tuple([x2, y2])}
            corners ^= {tuple([x1, y2])}
            corners ^= {tuple([x2, y1])}
            
        corners = list(corners)
        corners.sort()
        return len(corners) == 4 and (corners[1][1] - corners[0][1]) * (corners[2][0] - corners[1][0]) == total_area