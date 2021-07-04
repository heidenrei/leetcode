from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, A, k: int) -> int:
        R, C = len(A), len(A[0])
        pfs = [[0]* (C+1) for _ in range(R+1)]
        
        for x in range(R):
            for y in range(C):
                pfs[x+1][y+1] += pfs[x+1][y] + A[x][y]
                
        for x in range(R):
            for y in range(C):
                pfs[x+1][y+1] += pfs[x][y+1]
        
        best = -math.inf
        
        for x1 in range(R):
            for x2 in range(x1, R):
                sl = SortedList()
                sl.add(0)
                for y in range(C):
                    curr = pfs[x2+1][y+1] - pfs[x1][y+1]
                    t = curr - k
                    idx = sl.bisect_left(t)
                    
                    if 0 <= idx < len(sl):
                        best = max(best, curr - sl[idx])
                        
                    sl.add(curr)
                    
        return best