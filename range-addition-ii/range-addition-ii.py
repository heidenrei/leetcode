class Solution:
    def maxCount(self, R, C, ops):
        if not ops:
            return R * C
        minx = math.inf
        miny = math.inf
        
        for x, y in ops:
            minx = min(minx, x)
            miny = min(miny, y)
            
        return minx*miny
            
        