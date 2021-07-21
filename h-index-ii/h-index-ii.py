import bisect

class Solution:
    def hIndex(self, A):
        N = len(A)
        if N == 1:
            if A[0] == 0:
                return 0
            else:
                return 1
            
        if A[0] >= N:
            return N
        
        l = 0
        r = N
        while l < r:
            m = l + r >> 1
            i = bisect.bisect_left(A, m)
            if N-i >= m:
                l = m + 1
            else:
                r = m
                
        return l - 1