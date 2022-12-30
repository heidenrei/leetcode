# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        best = inf
        def has1(i):
            l, r = 0, C-1
            while l <= r:
                m = l + r >> 1
                if binaryMatrix.get(i, m):
                    r = m - 1
                else:
                    l = m + 1
            
            if r+1 < C and binaryMatrix.get(i, r+1):
                return r+1
            return inf
        
#         l, r = 0, R-1
#         while l < r:
#             m = (l + (r-l+1)) >> 1
#             ret, idx = has1(m)
#             if ret:
#                 r = m - 1
#             else:
#                 l = m
        for i in range(R):
            best = min(best, has1(i))
        return best if best < inf else -1
                
        
                
        
        
        