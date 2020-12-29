class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        xs = []
​
        ys = []
        
        for x1, y1, x2, y2 in rectangles:
            xs.append(x1)
            xs.append(x2)
            ys.append(y1)
            ys.append(y2)
            
        xlookup = {x: i for i, x in enumerate(sorted(set(xs)))}
        ylookup = {y: i for i, y in enumerate(sorted(set(ys)))}
        
        M = len(ylookup) - 1
        N = len(xlookup) - 1
        
        grid = [[0] * M for _ in range(N)]
        
        for x1, y1, x2, y2 in rectangles:
            for x_cell in range(xlookup[x1], xlookup[x2]):
                for y_cell in range(ylookup[y1], ylookup[y2]):
                    grid[x_cell][y_cell] += 1
                    
        for row in grid:
            for cell in row:
                if cell != 1:
                    return False
                
        return True
