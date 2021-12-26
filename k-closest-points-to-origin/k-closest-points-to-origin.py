import math

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points or not K:
            return
        
        res = []
        
        for p in points:
            res.append(self.helper(p))
            
        res = list(sorted(res, key=lambda x: x[0]))
        
        return [x[1] for x in res[:K]]
        
    def helper(self, points):
        return [math.sqrt(points[0]**2+points[1]**2), points]